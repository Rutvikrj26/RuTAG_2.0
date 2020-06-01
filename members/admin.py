from django.contrib import admin
from .models import Member, contact
# Register your models here.

admin.site.register(Member)

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):

    list_display = ["name","email","query", "date"]

    list_display_links = ["name","date"]

    search_fields = ["name"]

    list_filter = ["date"]
    class Meta:
        model = contact
