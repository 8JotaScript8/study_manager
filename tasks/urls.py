from django import views
from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, complete_task, uncomplete_task
from .views import DashboardView



urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'), 

    path('complete/<int:pk>/', complete_task, name='complete_task'), 
    path('uncomplete/<int:pk>/', uncomplete_task, name='uncomplete_task'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]