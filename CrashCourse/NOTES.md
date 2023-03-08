# Django Notes

Goal is to learn django and build a simple todo web app in a short time.

## Install django and create a project

### Install

1. Install Django `pip install django`
2. Create a Project `django-admin startproject mysite`
3. Cd into the project `cd mysite`

### Run

1. python migrate `python manage.py migrate`  
    - notes: this will create a database called db.sqlite3
2. Start the server `python manage.py runserver`
    - notes: this will run the server on port 8000
    - notes: we can change the port by running `python manage.py runserver 8080`

### Virtual environment

1. install `pip install virtualenv`
2.Create a virtual environment `virtualenv venv`
1. Activate the virtual environment windows: `source venv/Scripts/activate`

## Project Structure

1. **dont touch** `manage.py` = command line utility || command center

2. `settings.py` = main configuration file || command center
   - apps
   - middleware
   - template
   - database

3. `urls.py` = main url file || router
    - url patterns
    - url handlers
4. **dont touch** `wsgi.py` = web server gateway interface || entry point
5. **dont touch** `asgi.py` = asynchronous web server gateway interface || entry point

- Project is made of multiple apps(like a mini project) and each app has its own structure
- Inside the app sits all the models, template, urls, models
- Example: user, marketplace ect...
- We have to register each app in the settings file

## Project Structure for python manage.py startapp <APP_NAME>

1. Don't touch `__init__.py` = tells python that this is a package

## urls and views

- urls.py is the router
- each route executes a function that returns an html page
- Types of views: func/class
  - 1. function based views

    ```python
    def project(request, pk):
        return HttpResponse(f"Single project {pk}")

    # here we put a function in the view 
    urlpatterns = [
        path("project/<str:pk>", project, name="project"),
    ]
    ```

  - 2. Class based views

     ```python
    class ProjectView(View):
        def get(self, request, pk):
            return HttpResponse(f"Single project {pk}")

    # here we put a class in the view 
    urlpatterns = [
        path("project/<str:pk>", ProjectView.as_view(), name="project"),
    ]
    ```

### views.py

```python
def projects(request):
    return HttpResponse("Here are your products ")


def project(request, pk):
    return HttpResponse(f"Single project {pk}")
```

### Including views fom apps in the main app

```python
  from django.urls import path, include

  urlpatterns = [ path("", include("projects.urls"))]
```

```python
# the urls of the app
from django.urls import path
# from .views import projects, project or 
import . from views
urlpatterns = [
    path("projects/", views.projects, name="projects"),
    path("project/<str:pk>", views.project, name="project"),
]
```

### Templates

- create template folder next to the main app
- Register it in the settings.py file

```python

def projects(request):
    return render(request, "projects.html")

def project(request, pk):
    return render(request, "single-project.html")
```

#### Template inheritance

- Django uses something called JINJA2
- For example navigation `{% include 'navbar.html' %}` inside the html file

- standing templates

```html
<!-- child.html -->
{% extends 'main.html' %}

{% block content%}
<h1>Projects</h1>
{% endblock content%}
```

```html
<!-- main.html -->
<body>
    <h1>This is the main template</h1>
    {% block content%}

    {% endblock content%}
</body>
```

#### Separating Templates

##### Create a folder called templates inside app_name nad then another folder called "app_name"

- update the views to return the correct template

```python
def projects(request):
    return render(request, "projects/projects.html")

```

```html
<!-- templates/app_name/index.html -->

```

### Add App

1. Create an **app** called 'todolist' in the project `python manage.py startapp todolist`
2. Add the app to settings.py inside the main app under  `INSTALLED_APPS`

## Models

- each model maps to a database table
  
```python
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
```

## Views

- we want to hit an endpoint and get our todos
- **for each view we need to register a url**

```python
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {"todo_list": todos})

```

## urls

1. we need to register the urls in side the url file
2. we need to register the urls in the main app urls.py file

-

```python
#  inside the main app we can register our urls and our other app urls 
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todolist.urls")),
]

# ------------------------------------------------
# inside the app we can register our urls
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
```

## setup the admin page

0. `python manage.py migrate`
1. `python manage.py makemigrations`
2. create super user `python manage.py createsuperuser` and follow the instructions
3. in the admin file created register your todo models

```python
from django.contrib import admin
from .models import Todo

# Register your models here.

admin.site.register(Todo)

```

## Templates

1. create a folder called `templates` inside the main app and inside the `todolist` app
2. create a file called `index.html` inside the `templates` folder
3. Add the templates folder to the settings.py file

## querying

- inside the view

```python
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, "index.html", {"todo_list": todos})
```

## Summary

- Create models and register them in the admin page
- Create views and register them in the ur
- Create templates and register them in the settings.py file
- **ONLY FIRST TIME**Create app urls and register them in the main app urls
Note: in views `add/` vs `add` the `/` is important as it means its will be getting a collection of todos and not a single todo
