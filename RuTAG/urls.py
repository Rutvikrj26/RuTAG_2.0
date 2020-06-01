"""RuTAG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from article import views
from members.views import contactpage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name= "index" ),
    path('about', views.about, name="about"),
    path('Publications', views.Publications, name="Publications"),
    path('members/', include("members.urls")),
    path('Collaborators', views.Collaborators, name="Collaborators"),
    path('articles/', include("article.urls")),
    path('user/', include("user.urls")),
    path('events/',include("events.urls")),
    path('projects/',include("projects.urls")),
    path('products/',include("products.urls")),
    path('contact', contactpage, name="contact")
]

from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)