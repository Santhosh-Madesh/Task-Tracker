from django.db import models
from datetime import datetime

class TaskModel(models.Model):
    title = models.CharField()
    content = models.CharField()
    deadline = models.DateField()
    completed = models.BooleanField(null=True)

    def is_overdue(self):
        return datetime.now()<self.deadline