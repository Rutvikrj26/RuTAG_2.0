from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

Event_types = (('1', 'Core Group Meeting'),('2', 'Club Meeting'),('3', 'Workshop'),('4', 'Staff & PI Meetings'),('6','Other Events') )

class Event(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Writer")
    organizer = models.CharField(max_length=50,verbose_name = "Organizer")
    location = models.CharField(max_length=100,verbose_name= "Location where the event was held")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    Event_date = models.DateTimeField(verbose_name="Event Date")
    Event_poster = models.FileField(blank = True,null = True,verbose_name="Add Photo to Event")
    Event_type = models.CharField(max_length=50,choices=Event_types)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-Event_date','-Event_type']
