from django.contrib import admin

# Register your models here.

from .models import Category, Client, Project, Team, Post


admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Team)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publish', 'status')
	prepopulated_fields = {'slug': ('title',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'client')