from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.ProjectListView.as_view(), name='portfolio'),
    path('content/<slug:id>/<slug:category>/<slug:client>/', views.project_content, name='project_content'),

]
