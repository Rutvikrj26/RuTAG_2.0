from django import forms
from .models import Event, event_report

class EventFileForm(forms.ModelForm):
    class Meta:
        model = event_report
        fields = ["Event_report"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title","organizer","Event_date","Event_type","content","location"]