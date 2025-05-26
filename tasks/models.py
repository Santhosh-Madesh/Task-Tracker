from django.db import models
from datetime import date

class TaskModel(models.Model):
    title = models.CharField()
    content = models.CharField()
    deadline = models.DateField()
    completed = models.BooleanField(null=True)

    def is_overdue(self):
        return date.today()>self.deadline