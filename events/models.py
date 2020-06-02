from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

Event_types = (('0', 'Core Group Meeting'),('1', 'Club Meeting'),('2', 'Workshop'),('3', 'Staff & PI Meetings'),('4','Other Events') )

class Event(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Writer")
    organizer = models.CharField(max_length=50,verbose_name = "Organizer")
    location = models.CharField(max_length=100,verbose_name= "Location where the event was held")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField(verbose_name="Enter the Event Details Here")
    Event_date = models.DateTimeField(verbose_name="Event Date & time", blank=True,null=True)
    Event_type = models.CharField(max_length=50,choices=Event_types)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-Event_date','-Event_type']

class event_report(models.Model):
    Event_report = models.FileField(blank=True, null=True, verbose_name="Enter the report here")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
