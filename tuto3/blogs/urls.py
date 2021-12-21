from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='index'),
    path('content/<slug:id>/<slug:category>/<slug:client>/', views.project_content, name='project_content'),

]
