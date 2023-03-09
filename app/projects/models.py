from django.db import models

# Create your models here.

import uuid


class Project(models.Model):
    title = models.CharField(max_length=100)
    # the black is for the user to not have to fill it out and the null is for the database to not have to fill it out
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    # Many to many relationship
    # Since the class is not defined yet, we use a string and that delays it until the class is defined
    tags = models.ManyToManyField("Tag", blank=True)

    # I want to have  vote_total field here
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    # immutable fields
    VOTE_TYPE = (("up", "Up Vote"), ("down", "Down Vote"))
    # Owner
    # Project

    # This is a one project to many reviews relationship (one to many) meaning it needs the ForeignKey of the project aka parent
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )  # delete all the reviews if the project is deleted

    body = models.TextField(max_length=1000)
    value = models.CharField(max_length=100)

    # Time stamp and the Id
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.value


class Tag(models.Model):

    name = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name
