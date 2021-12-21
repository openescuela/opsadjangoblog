from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect

from .models import Project

class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'projects'
    queryset = Project.objects.all()
    template_name = 'blogs/index.html'

def project_content(request, id, category, client):
    project = get_object_or_404(Project, id=id, category__name = category, client__name = client)
    return render(request, 'blogs/content.html', {'project':project})
