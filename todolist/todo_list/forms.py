
from django import forms
from django.contrib.auth.models import User
from .models import Task


class TaskDueDate(forms.DateInput):
    input_type = 'datetime-local'


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "notes", "deadline"]
        widgets = {"deadline": TaskDueDate()}
