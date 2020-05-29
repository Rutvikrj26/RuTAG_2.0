from django.contrib import admin
from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addproject/', views.addProject, name="addproject"),
    path('project/<int:id>', views.detail, name="project_detail"),
    path('update/<int:id>', views.updateProject, name="update"),
    path('delete/<int:id>', views.deleteProject, name="delete"),
    path('', views.projects, name="projects"),

]
