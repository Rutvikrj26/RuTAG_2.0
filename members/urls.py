from django.contrib import admin
from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path('',views.members, name="members"),
    path('club',views.club, name = "club"),
    path('core', views.core, name="core"),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)