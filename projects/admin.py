from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Project, professor, student, engineer

# Register your models here.

admin.site.register(professor)
admin.site.register(student)
admin.site.register(engineer)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ["title","professor","Project_date","engineer","student"]

    list_display_links = ["title","Project_date"]

    search_fields = ["title"]

    list_filter = ["Project_date"]
    class Meta:
        model = Project

