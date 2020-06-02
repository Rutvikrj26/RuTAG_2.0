from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Event, event_report

# Register your models here.

class EventreportInline(admin.TabularInline):
    model = event_report

class EventreportAdmin(admin.ModelAdmin):
    inlines = [
        EventreportInline,
    ]

admin.site.register(Event, EventreportAdmin)

