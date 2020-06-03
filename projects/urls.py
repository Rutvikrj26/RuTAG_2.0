from django.contrib import admin
from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addproject/', views.addProject, name="addproject"),
    path('projects/<int:id>', views.detail, name="project_detail"),
    path('update/<int:id>', views.updateProject, name="update"),
    path('delete/<int:id>', views.deleteProject, name="delete"),
    path('proposed', views.proposed, name="proposed"),
    path('in_pipeline', views.in_pipeline, name="in_pipeline"),
    path('completed', views.completed, name="completed"),
    path('executed', views.executed, name="executed"),
    path('about/', views.about, name="about"),
]
