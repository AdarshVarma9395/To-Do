from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_User

@login_required(login_url='login')
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'myapp/list.html', context)


@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render(request, 'myapp/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task':task}
    return render(request, 'myapp/delete.html', context)

@unauthenticated_User
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'myapp/register.html',  context)

@unauthenticated_User
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username OR Password is incorrect')
    context = {}
    return render(request, 'myapp/login.html',  context)


def logoutPage(request):
    logout(request)
    return redirect('login')