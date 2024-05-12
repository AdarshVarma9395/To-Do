from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import TaskForm

def index(request):
    task = Task.objects.all()
    context = {'tasks':task}
    return render(request, 'myapp/list.html', context)


def createTask(request):
    form = TaskForm()
    context = {'form':form}

    return render(request, 'myapp/taskform.html', context)