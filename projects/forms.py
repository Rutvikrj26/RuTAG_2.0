from django import forms
from .models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title","professor","student","engineer","Project_date","status","content","Project_poster","Project_report"]

from django import forms
from .models import professor, student


class ProjectChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    professor = forms.ModelMultipleChoiceField(
        queryset=professor.objects.all(), required=False)
    student = forms.ModelMultipleChoiceField(
        queryset=student.objects.all(), required=False)