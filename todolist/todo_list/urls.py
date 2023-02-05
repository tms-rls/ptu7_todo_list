
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('register/', views.register, name='register'),
    path('mytasks/', views.TasksByUserListView.as_view(), name='my_tasks'),
    path('mytasks/<int:pk>', views.TaskByUserDetailView.as_view(), name='my_specific_task'),
    path('mytasks/new', views.TaskByUserCreateView.as_view(), name='my_tasks_new'),
    path('mytasks/<int:pk>/update', views.TaskByUserUpdateView.as_view(), name='my_tasks_update'),
    path('mytasks/<int:pk>/delete', views.TaskByUserDeleteView.as_view(), name='my_tasks_delete'),
]
