from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect

from .models import Project, Team

def index(request):
    return render(request, 'blogs/index.html')

def service(request):
    return render(request, 'blogs/service.html')

class ProjectListView(generic.ListView):
    model = Project

class TeamListView(generic.ListView):
    model = Team
    context_object_name = 'teams'
    queryset = Team.objects.all()
    template_name = 'blogs/team.html'

def project_content(request, id, category, client):
    project = get_object_or_404(Project, id=id, category__name = category, client__name = client)
    return render(request, 'blogs/content.html', {'project':project})
