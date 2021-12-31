from django.contrib import admin

# Register your models here.

from .models import Category, Client, Project, Team

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Team)
