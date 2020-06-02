from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Product, organization, product_image

# Register your models here.

admin.site.register(organization)

class ProductimageInline(admin.TabularInline):
    model = product_image

class ProductimageAdmin(admin.ModelAdmin):
    inlines = [
        ProductimageInline,
    ]

admin.site.register(Product, ProductimageAdmin)