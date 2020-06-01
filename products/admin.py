from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Product, organization

# Register your models here.

admin.site.register(organization)

@admin.register(Product)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ["title","organization"]

    list_display_links = ["title"]

    search_fields = ["title"]

    list_filter = ["organization"]
    class Meta:
        model = Product