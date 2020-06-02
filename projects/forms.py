from django import forms
from .models import Project, project_report
from django.forms import ClearableFileInput

from django import forms

class FileProjectFormreport(forms.ModelForm):
    class Meta:
        model = project_report
        fields = ["Project_report"]
        widgets = {
            'Project_report': ClearableFileInput(attrs={'multiple': True}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title","professor","student","engineer","Project_date","status","content"]

