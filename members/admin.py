from django.contrib import admin
from .models import Member, contact, index_images
# Register your models here.

admin.site.register(Member)
admin.site.register(index_images)
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):

    list_display = ["name","email","query", "date"]

    list_display_links = ["name","date"]

    search_fields = ["name"]

    list_filter = ["date"]
    class Meta:
        model = contact
