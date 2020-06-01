from django.contrib import admin
from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path('',views.members, name="members"),
    path('club',views.club, name = "club"),
    path('core', views.core, name="core"),
]

