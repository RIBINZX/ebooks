from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Product,Comment



admin.site.register(Product)
admin.site.register(Comment)

