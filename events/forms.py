from django import forms
from .models import Event
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title","organizer","Event_date","Event_type","content","location","Event_poster"]