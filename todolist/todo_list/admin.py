from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'user', 'deadline']
    list_filter = ['user']
    search_fields = ['name', 'user', 'deadline']


admin.site.register(Task, TaskAdmin)
