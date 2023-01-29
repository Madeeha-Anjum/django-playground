from django.db import models

# create models here


class Books(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    # this means that when we call the object, it will return the title
    def __str__(self):
        return self.title


# /books/list
