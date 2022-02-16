from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect

from .models import Project, Team, Post

from django.core.paginator import Paginator

from django.db.models import Q

from .forms import CommentForm

def index(request):
    return render(request, 'blogs/index.html')

def service(request):
    return render(request, 'blogs/service.html')

def portfolio(request, category, client):
    if category == 'all' and client == 'all':
        projects = Project.objects.all()
    elif category == 'all':
        projects = Project.objects.filter(client__name = client)
    else:
        projects = Project.objects.filter(category__name = category)
    paginator = Paginator(projects, 3)
    page = request.GET.get('page')
    projects_page = paginator.get_page(page)
    return render(request, 'blogs/project_list.html', {'projects':projects_page})

class TeamListView(generic.ListView):
    model = Team
    context_object_name = 'teams'
    queryset = Team.objects.all()
    paginate_by = 1
    template_name = 'blogs/team.html'

def project_detail(request, id, category, client):
    project = get_object_or_404(Project, id=id, category__name = category, client__name = client)
    return render(request, 'blogs/project_detail.html', {'project':project})

def forum(request, category):
    if category == 'all':
        posts = Post.objects.filter(status='published')
    else:
        posts = Post.objects.filter(status='published', category__name = category)
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts_page = paginator.get_page(page)
    return render(request, 'blogs/post_list.html', {'posts':posts_page})

def post_detail(request, slug, year, month, day):
    post = get_object_or_404(Post, slug=slug, publish__year = year, publish__month = month, publish__day = day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(request.path)
    else:
        comment_form = CommentForm()
    return render(request, 'blogs/post_detail.html', {'post':post,'comments':comments,'comment_form':comment_form})

class PostSearchListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blogs/post_search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query is not None:
            queryset = Post.objects.filter((Q(title__icontains=query) | Q(resume__icontains=query)), status='published')
            return queryset
        else :
            return Post.objects.filter(status='published').none() # just an empty queryset as default

def project_search(request):
    if request.GET.get('query'):
        query_name =  request.GET.get('query')
        try:
            projects = Project.objects.filter(Q(name__icontains=query_name) | Q(resume__icontains=query_name))
            paginator = Paginator(projects, 2)
            page = request.GET.get('page')
            projects_page = paginator.get_page(page)
            return render(request,'blogs/project_search.html', {'projects': projects_page, 'query': query_name})
        except:
            return render(request,'blogs/project_search.html')
    else:
        return render(request,'blogs/project_search.html')



'''
class ProjectSearchListView(generic.ListView):
    model = Project
    context_object_name = 'projects'
    paginate_by = 1
    template_name = 'blogs/project_search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query is not None:
            queryset = Project.objects.filter(Q(name__icontains=query))
            return queryset
        else :
            return Project.objects.none() # just an empty queryset as default
'''
