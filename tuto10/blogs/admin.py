from django.contrib import admin

# Register your models here.

from .models import Category, Client, Project, Team, Post, Comment, PostCategory


admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(PostCategory)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publish', 'status')
	prepopulated_fields = {'slug': ('title',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'client')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
