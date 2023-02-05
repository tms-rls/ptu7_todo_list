
from django.db import models
from django.contrib.auth.models import User
import datetime
import pytz


utc = pytz.UTC


class Task(models.Model):
    name = models.CharField(verbose_name='Task', max_length=300, help_text='Insert task text')
    notes = models.TextField(verbose_name='Task notes', max_length=3000, null=True, blank=True,
                             help_text='Insert task notes')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name='Date and time of insertion', auto_now_add=True)
    deadline = models.DateTimeField(verbose_name='Task deadline', null=True, blank=True)

    def due_date(self):
        if self.deadline:
            return datetime.datetime.today().replace(tzinfo=utc) > self.deadline.replace(tzinfo=utc)
        else:
            return False

    def __str__(self):
        return self.name
