from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Article,Comment,newsletter_File,Newsletter

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta:
        model = Article

class NewsletterfileInline(admin.TabularInline):
    model = newsletter_File

class NewsletterfileAdmin(admin.ModelAdmin):
    inlines = [
        NewsletterfileInline,
    ]

admin.site.register(Newsletter, NewsletterfileAdmin)
