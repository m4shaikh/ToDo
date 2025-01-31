from django.shortcuts import render , redirect , get_object_or_404
from .models import Task
# Create your views here.
from django.utils.timezone import now

def task_list(request):
    tasks = Task.objects.all()
    return render(request ,'tasks/task_list.html', {'tasks': tasks})

def add_tasks(request):
    if request.method ==  'POST':
        name = request.POST.get('name')
        detail = request.POST.get('detail')
        Task.objects.create(name=name , detail=detail)
        return redirect('task_list')
    return render(request, 'tasks/task_add.html')


def delete_task(request , task_id):
    if request.method == 'POST':
        task = get_object_or_404( Task , id = task_id )
        task.delete()
        return redirect('task_list')
    
def complete(request , task_id):
    
    task = get_object_or_404(Task , id = task_id)
    
    if request.method == 'POST':
        task.is_completed = True
        task.completed_at = now()
        task.save()
        return redirect('task_list')
    

def update_task(request , task_id):
    
    task = get_object_or_404(Task , id = task_id)
    
    if request.method == 'POST':
        task.name = request.POST.get('name')
        task.detail  = request.POST.get('details')
        task.save()
    
        return redirect('task_list')
    
    return render(request, 'tasks/task_update.html', {'task': task})