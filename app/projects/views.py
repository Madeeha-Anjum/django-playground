from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


# Create your views here.

from django.http import HttpResponse


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    print(projects)
    return render(request, "projects/projects.html", context)
    # return HttpResponse("Here are your products ")


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    print(projects)
    return render(request, "projects/single-project.html", context)

    # return HttpResponse(f"Single project {pk}")


def createProject(request):
    form = ProjectForm()

    if request.method == "post":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()  # save the form to the database

    context = {"form": form}
    # print the form types
    print("the form object", form)
    print("Create Project")
    return render(request, "projects/project_form.html", context)
