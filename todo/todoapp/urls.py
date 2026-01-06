from django.contrib import admin
from django.urls import path
from .views import index, list_detail, create_task, create_list, toggle_task, delete_list, delete_task, edit_task

urlpatterns = [
    path('', index, name='index'),
    path('list/<int:list_id>/', list_detail, name='list_detail'),
    path('list/<int:list_id>/create_task/', create_task, name='create_task'),
    path('create_list/', create_list, name='create_list'),
    path('task/<int:task_id>/toggle/', toggle_task, name='toggle_task'),
    path('list/<int:list_id>/delete/', delete_list, name='delete_list'),
    path('task/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('task/<int:task_id>/edit/', edit_task, name='edit_task'),

]