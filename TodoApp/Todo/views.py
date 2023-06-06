from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def index(request):
    todo_task = Todo.objects.all()
    context = {"todotask": todo_task}
    return render(request, "todo/todo.html", context)

def add_task(request):
    return render(request, 'todo/addTask.html')

def details(request, id):
    todo = Todo.objects.get(id= id)
    context = {'todo_task': todo}
    return render(request, 'todo/details.html', context)

def submit(request):
    todo_title= request.POST['title']
    todo_body = request.POST['body']
    todo_task = Todo(title=todo_title, task=todo_body).save()

    return redirect('/todo/')


def delete(request, id ):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect('/todo/')