from django.db import models

class TaskModel(models.Model):
    title = models.CharField()
    content = models.CharField()
    deadline = models.DateField()
