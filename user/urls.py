from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('Events/',views.Events,name = 'Events'),
    path('Publications/', views.Publications, name='Publications'),
    path('Projects/', views.Projects, name='Projects'),
    path('IPD/', views.IPD, name='IPD'),
    path('News/', views.News, name='News'),
    path('Collaborators/', views.Collaborators, name='Collaborators'),
    path('Conferences/', views.Conferences, name='Conferences'),
    path('RuTAG_Club/', views.RuTAG_Club, name='RuTAG_Club'),

]
