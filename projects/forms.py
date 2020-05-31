from django import forms
from .models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title","professor","student","engineer","Project_date","status","content","Project_poster","Project_report"]
