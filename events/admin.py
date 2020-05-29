from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Event

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ["title","organizer","Event_date","location"]

    list_display_links = ["title","Event_date"]

    search_fields = ["title"]

    list_filter = ["Event_date"]
    class Meta:
        model = Event

