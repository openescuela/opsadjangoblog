
from django import template
from ..models import Project, Team

register = template.Library()

@register.simple_tag
def show_n_portfolio(count=3):
    projects = Project.objects.all()[:count]
    return projects

@register.simple_tag
def show_n_team(count=3):
    teams = Team.objects.all()[:count]
    return teams
