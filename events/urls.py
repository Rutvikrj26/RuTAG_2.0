from django.contrib import admin
from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addevent/', views.addEvent, name="addevent"),
    path('event/<int:id>', views.detail, name="event_detail"),
    path('update/<int:id>', views.updateEvent, name="update"),
    path('delete/<int:id>', views.deleteEvent, name="delete"),
    path('', views.events, name="events"),
    path('workshops', views.workshop, name="workshop"),
    path('CoreGroupMeetings', views.cgm, name="cgm"),
    path('Staff&PIMeetings', views.spm, name="spm"),
    path('otherEvents', views.other, name= "other"),
]
