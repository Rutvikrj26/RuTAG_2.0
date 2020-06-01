from django import forms
from .models import Product,organization

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title","organization","content",]

class organizationForm(forms.ModelForm):
    class Meta:
        model = organization
        fields = ["name","contact","email","profilepic",]