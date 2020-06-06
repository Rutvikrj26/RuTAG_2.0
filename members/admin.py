from django.contrib import admin
from .models import Member, contact, index_images, news, writeup
# Register your models here.

admin.site.register(Member)
admin.site.register(index_images)
admin.site.register(news)
admin.site.register(writeup)
admin.site.register(contact)
