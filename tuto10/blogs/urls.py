from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('portfolio/<slug:category>/<slug:client>/', views.portfolio, name='portfolio'),
    path('team/', views.TeamListView.as_view(), name='team'),
    path('project/<slug:id>/<slug:category>/<slug:client>/', views.project_detail, name='project_detail'),
    path('post/<slug:category>/', views.forum, name='post_list'),
    path('post/<slug:slug>/<int:year>/<int:month>/<int:day>/', views.post_detail, name='post_detail'),
    path('post/serach/', views.PostSearchListView.as_view(), name='post_search'),
    path('project/search/', views.project_search, name='project_search'),
    #path('project/serach/', views.ProjectSearchListView.as_view(), name='project_search'),

]
