from django import forms


class contactForm(forms.Form):
    name = forms.CharField(max_length=50, label="name")
    email = forms.EmailField(max_length=20, label="email")
    query = forms.CharField(widget=forms.Textarea)