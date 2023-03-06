from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, "index.html", {"todo_list": todos})


@require_http_methods(["POST"])
def add(request):
    title = request.POST.get("title")
    todos = Todo.objects.create(title=title)
    todos.save()
    return redirect("index")


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.complete
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")
