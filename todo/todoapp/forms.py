from .models import List, Task
from django import forms

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'date']
       

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'list']