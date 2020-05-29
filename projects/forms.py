from django import forms
from .models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title","professor","student","Project_date","content","Project_poster","Project_report"]
