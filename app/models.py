from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField


class Category(models.Model):
    title = models.CharField(max_length=20)
    created_date = models.DateField(default = date.today())
    active = models.BooleanField(default=True)


class Article(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_date = models.DateField(date.today())
    image = models.ImageField(default="profile_pics/default.xyz", upload_to="profile_pics")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
