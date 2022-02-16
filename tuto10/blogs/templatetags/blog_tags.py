
from django import template
from ..models import Project, Team, PostCategory, Post, Category, Client
from urllib.parse import urlencode
from django.db.models import Count

register = template.Library()

@register.simple_tag
def show_n_portfolio(count=3):
    projects = Project.objects.all()[:count]
    return projects

@register.simple_tag
def show_n_team(count=3):
    teams = Team.objects.all()[:count]
    return teams

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

@register.simple_tag
def show_list_postcategory():
    return PostCategory.objects.all()

@register.simple_tag
def get_most_commented_posts(count=4):
    publishedpost = Post.objects.filter(status='published')
    return publishedpost.annotate( total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.simple_tag
def show_list_projectcategory():
    return Category.objects.all()

@register.simple_tag
def show_list_projectclient():
    return Client.objects.all()
