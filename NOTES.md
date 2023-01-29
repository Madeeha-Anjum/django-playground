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

## setup the admin page

1. `python manager.py makemig
1. `python manage.py createsuperuser`
