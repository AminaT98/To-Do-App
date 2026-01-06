from django.db import models
from datetime import date

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ForeignKey('List', related_name='tasks', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title
    
class List(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, default='To-Do List')
   
    def __str__(self):
        return self.name