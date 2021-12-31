from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.ProjectListView.as_view(), name='portfolio'),
    path('team/', views.TeamListView.as_view(), name='team'),
    path('content/<slug:id>/<slug:category>/<slug:client>/', views.project_content, name='project_content'),

]
