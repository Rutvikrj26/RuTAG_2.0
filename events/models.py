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
    Event_date = models.DateTimeField(verbose_name="Event Date & time")
    Event_poster = models.FileField(blank = True,null = True,verbose_name="Add Photo to Event")
    Event_type = models.CharField(max_length=50,choices=Event_types)
    Event_report = models.FileField(blank=True, null=True, verbose_name="Enter a combined document here")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-Event_date','-Event_type']
