# Django Notes

Goal is to learn django and build a simple web app in a short time.

## Install django and create a project

1. `pip install django`
2. `cd mysite`
3. `django-admin startproject mysite`
4. Create an app callled 'todolist' `python manage.py startapp todolist`
5 add it to the settings.py inside the main app under  `INSTALLED_APPS`
5. run the server `python manage.py runserver`
    - notes: this will run the server on port 8000
    - notes: we can change the port by running `python manage.py runserver 8080`

## models

- each model maps to a database table
  
```python
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
```

## Views

- we want to hit an endpoint and get our books
- **for each view we need to register a url**

```python
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {"todo_list": todos})

```

## urls

```python
from django.urls import path, include 
from . import views

#  inside the main app we can register our urls and our other app urls 
urlpatterns = [
    path('', views.index, name='index'),
    path('todolist/', include('todolist.urls')),
]
```

## Templates

1. create a folder called `templates` inside the main app and inside the `todolist` app
2. create a file called `index.html` inside the `templates` folder
3. Add the templates folder to the settings.py file

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

## querying

- inside the view

```python
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, "index.html", {"todo_list": todos})
```
