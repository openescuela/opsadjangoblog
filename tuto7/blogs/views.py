from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect

from .models import Project, Team, Post

from django.core.paginator import Paginator

def index(request):
    return render(request, 'blogs/index.html')

def service(request):
    return render(request, 'blogs/service.html')

class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 2

class TeamListView(generic.ListView):
    model = Team
    context_object_name = 'teams'
    queryset = Team.objects.all()
    paginate_by = 1
    template_name = 'blogs/team.html'

def project_content(request, id, category, client):
    project = get_object_or_404(Project, id=id, category__name = category, client__name = client)
    return render(request, 'blogs/content.html', {'project':project})

def forum(request):
	posts = Post.objects.filter(status='published')
	paginator = Paginator(posts, 1) 
	page = request.GET.get('page')
	posts_page = paginator.get_page(page)
	return render(request, 'blogs/post_list.html', {'posts':posts_page})

def post_detail(request, slug, year, month, day):
	post = get_object_or_404(Post, slug=slug, publish__year = year, publish__month = month, publish__day = day)
	return render(request, 'blogs/post_detail.html', {'post':post})