from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def projects(request):
    return render(request, "projects.html")
    # return HttpResponse("Here are your products ")


def project(request, pk):
    return render(request, "single-project.html")

    # return HttpResponse(f"Single project {pk}")
