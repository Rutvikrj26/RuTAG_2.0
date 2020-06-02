from django import forms
from .models import Article, Newsletter, newsletter_File

class newsletterFileForm(forms.ModelForm):
    class Meta:
        model = newsletter_File
        fields = ["Newsletter_file"]

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]
        