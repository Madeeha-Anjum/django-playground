from django.shortcuts import render


def index(request):
    return render(request, "index.html", {"todo_list": todos})
