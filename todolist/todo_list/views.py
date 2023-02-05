
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task
from .forms import TaskCreateForm


def statistics(request):
    num_tasks = Task.objects.all().count()
    context = {
        'num_tasks': num_tasks,
    }

    return render(request, 'start.html', context=context)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} is taken!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with email {email} is already registered!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} registered!')
                    return redirect('login')
        else:
            messages.error(request, "Passwords doesn't match!")
            return redirect('register')
    return render(request, 'register.html')


class TasksByUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'my_tasks.html'
    context_object_name = 'my_tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskByUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = 'my_specific_task.html'
    context_object_name = 'my_specific_task'


class TaskByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    success_url = '/mytasks/'
    template_name = 'my_task_form.html'
    form_class = TaskCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class TaskByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    template_name = 'my_task_form.html'
    form_class = TaskCreateForm

    def get_success_url(self):
        return reverse('my_specific_task', kwargs={"pk": self.object.id})

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class TaskByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    success_url = '/mytasks/'
    template_name = 'my_task_delete.html'
    context_object_name = 'my_specific_task'

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user
