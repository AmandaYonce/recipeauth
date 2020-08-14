from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    pass


class Recipe(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Author, null=True, on_delete = models.SET_NULL)
    description = models.TextField()
    time_Required = models.CharField(max_length=200, null=True)
    instructions = models.TextField()

    def __str__(self):
        return self.title



