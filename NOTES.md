# Django Notes

Goal is to learn django and build a simple todo web app in a short time.

## Install django and create a project

**Install**

1. Install Django `pip install django`
2. Create a Project `django-admin startproject mysite`
3. Cd into the project `cd mysite`

**Run**

1. python migrate `python manage.py migrate`  
    - notes: this will create a database called db.sqlite3
2. Start the server `python manage.py runserver`
    - notes: this will run the server on port 8000
    - notes: we can change the port by running `python manage.py runserver 8080`

**Add App**

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
