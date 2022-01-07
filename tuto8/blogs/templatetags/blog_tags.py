
from django import template
from ..models import Project, Team
from urllib.parse import urlencode

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