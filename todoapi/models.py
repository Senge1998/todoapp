from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    task_name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False, blank=True, null=True)
    completed_at = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.task_name