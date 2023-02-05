
from django.urls import path
from . import views

urlpatterns = [
    path('', views.statistics, name='start'),
    path('register/', views.register, name='register'),
    path('mytasks/', views.TasksByUserListView.as_view(), name='my_tasks'),
    path('mytasks/<int:pk>', views.TaskByUserDetailView.as_view(), name='my_specific_task'),
    path('mytasks/new', views.TaskByUserCreateView.as_view(), name='my_tasks_new'),
]
