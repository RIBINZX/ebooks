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
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.FloatField()
    year=models.IntegerField()
    image=models.ImageField(upload_to="")

    def __str__(self):
        return self.name
    




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.content