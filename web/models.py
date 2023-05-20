from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    LANG_CHOICES = (
        ('eng', 'English'),
        ('mal', 'Malayalam'),
        ('ara', 'Arabic'),
    )
    language = models.CharField(max_length=3, choices=LANG_CHOICES)
    author=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    year=models.IntegerField()
    image=models.ImageField(upload_to="")


