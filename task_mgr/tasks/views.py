from django.shortcuts import render
from django.utils import timezone
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.order_by('status', 'priority')

    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)