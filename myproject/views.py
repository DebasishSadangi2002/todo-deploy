from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from todo.forms import TodoItemForm
from todo.models import Task

# Create your views here.
@login_required
def list(request):
    tasks = Task.objects.filter(username=request.user)
    return render(request, 'list.html', {'tasks':tasks})

@login_required
def add_todo_view(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.username = request.user
            todo.save()
            return redirect('home')
    else:
        form = TodoItemForm()
    return render(request, 'add_todo.html', {'form': form})


@login_required
def update_todo_view(request, pk):
    todo = get_object_or_404(Task, pk=pk, username=request.user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'update_todo.html', {'form': form, 'todo': todo})

@login_required
def delete_todo_view(request, pk):
    todo = get_object_or_404(Task, pk=pk, username=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'delete_todo.html', {'todo': todo})



