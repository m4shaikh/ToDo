from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_tasks, name='add_tasks'),
    path('complete/<int:task_id>/',views.complete , name ='complete'),
    path('delete_task/<int:task_id>/', views.delete_task, name = 'delete_task'),
    path('update_task/<int:task_id>/', views.update_task, name = 'update_task')
]
