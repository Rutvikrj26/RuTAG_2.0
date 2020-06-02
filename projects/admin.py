from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Project, project_report

# Register your models here.

class ProjectreportInline(admin.TabularInline):
    model = project_report

class ProjectreportAdmin(admin.ModelAdmin):
    inlines = [
        ProjectreportInline,
    ]

admin.site.register(Project, ProjectreportAdmin)


