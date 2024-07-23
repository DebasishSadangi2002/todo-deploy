from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import TodoItemForm
from .models import Task

# Create your views here.
@login_required
def list(request):
    tasks = Task.objects.filter(username=request.user)
    return render(request, 'todo/list.html', {'tasks':tasks})

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
    return render(request, 'todo/add_todo.html', {'form': form})


@login_required
def update_todo_view(request, pk):
    todo = get_object_or_404(Task, pk=pk, username=request.user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:list')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo/update_todo.html', {'form': form, 'todo': todo})

@login_required
def delete_todo_view(request, pk):
    todo = get_object_or_404(Task, pk=pk, username=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'todo/delete_todo.html', {'todo': todo})
