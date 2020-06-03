from django import forms
from .models import Product,organization, product_image

class ProductFileForm(forms.ModelForm):
    class Meta:
        model = product_image
        fields = ["Product_image"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title","organization","content","short","Product_image"]

class organizationForm(forms.ModelForm):
    class Meta:
        model = organization
        fields = ["name","contact","email"]
