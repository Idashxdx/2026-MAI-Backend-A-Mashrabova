# LAB4
from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=100)


class Watch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User(AbstractUser):
    favorites = models.ManyToManyField(Watch, blank=True)
