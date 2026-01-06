from django.shortcuts import render, redirect, get_object_or_404
from .models import List, Task


# Create your views here.
def index(request):
    lists = List.objects.all()
    tasks = Task.objects.all()
    context = {
        'lists': lists,
        'tasks': tasks,
    }
    return render(request, 'index.html', context)

def list_detail(request, list_id):
    todo_list = List.objects.get(id=list_id)
    tasks = Task.objects.filter(list=todo_list)
    
       # Check if an edit request exists
    edit_task_id = request.GET.get('edit')
    edit_task = None
    if edit_task_id:
        edit_task = get_object_or_404(Task, id=edit_task_id)
    
    context = {
        'todo_list': todo_list,
        'tasks': tasks,
        'edit_task': edit_task, # pass this to the template
    }
    return render(request, 'list_detail.html', context)

def create_task(request, list_id):
    if request.method == 'POST':
        todo_list = List.objects.get(id=list_id)
        task_title = request.POST.get('title')
        task_description = request.POST.get('description', '')
        Task.objects.create(title=task_title, description=task_description, list=todo_list)
    return redirect('list_detail', list_id=list_id)

def create_list(request):
    if request.method != 'POST':
        return render(request, 'new_list.html')
    else:
        list_name = request.POST.get('name')
        list_date = request.POST.get('date')
        list = List.objects.create(name=list_name, date=list_date)
    return redirect('list_detail', list_id=list.id)

def toggle_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()

        return redirect('list_detail', list_id=task.list.id)

def delete_list(request, list_id):
    if request.method == "POST":
        todo_list = get_object_or_404(List, id=list_id)
        todo_list.delete()
        return redirect('index')
    
def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        list_id = task.list.id
        task.delete()
        return redirect('list_detail', list_id=list_id)
    
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST.get('title', task.title)
        task.description = request.POST.get('description', task.description)
        task.save()
        return redirect('list_detail', list_id=task.list.id)
    context = {
        'task': task,
    }
    return render(request, 'list_detail.html', context)