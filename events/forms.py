from django import forms
from .models import Event
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title","organizer","Event_date","content","location","Event_poster"]