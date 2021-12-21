from django.contrib import admin

# Register your models here.

from .models import Category, Client, Project

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Category)
