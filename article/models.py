from django.db import models
import django.utils.timezone
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Writer ")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
    article_image = models.FileField(blank = True,null = True,verbose_name="Add Photo to Article")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Name")
    comment_content = models.CharField(max_length = 200,verbose_name = "Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

class Newsletter(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Enter your news letter title here")
    created_date = models.DateTimeField(verbose_name="Creation Date", null=True, blank=True)
    description = RichTextField()
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class newsletter_File(models.Model):
    Newsletter_file = models.FileField(verbose_name="files of Newsletter Field")
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='files')

class Video(models.Model):
    title = models.CharField(max_length=500, verbose_name="title of video being entered")
    description = RichTextField(max_length=500, verbose_name="description if you want to give")
