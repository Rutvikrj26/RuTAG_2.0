from django.db import models
from ckeditor.fields import RichTextField

class contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="name of the person contacting")
    email = models.EmailField(verbose_name="email of the person contacting")
    position = models.CharField(max_length=100, verbose_name="Query of the person", null=True, blank=True)
    phone = models.CharField(max_length=25,verbose_name="Phone number of the Contact", null=True, blank= True)


positions = (('0','RuTAG Club - trainee'), ('1','RuTAG Club - Project Member'), ('2', 'RuTAG Club - Project Leader'),
             ('3', 'RuTAG Club - Club Coordinator'),('4', 'RuTAG Club - Club principal'),('5', 'RuTAG Club - Club Secratary'),
             ('6', 'Core - Jr. Project Assistant'), ('7', 'Core - Sr. Project Assistant'), ('8', 'Core - Club Principal Inspector'), ('9', 'Core - Chairman'), ('10', 'Core - PI'),
             ('11', 'Core - Jr. Project Attendant'), ('12','Core - Project Associate'), ('13', 'Core - Coordinator and Principal Investigator (PI)'), ('14', 'Core - Chairman, Core Group'),('15', 'Core - Web Developer'), ('16','Research Scholar'))

levels = [(i,i) for i in range(8)]

class Member(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name of the Member")
    position = models.CharField(max_length=50, verbose_name="position of the member")
    image = models.ImageField(verbose_name="Profile Picture of the Member", default='/static/default.jpg')
    detail = models.TextField(verbose_name="Some detail about the Member", null=True,blank=True)
    email = models.EmailField(verbose_name="email id of the member", default="rutagiitd@gmail.com")
    work = models.CharField(max_length=20, choices=(('0', 'Core'), ('1', 'Club')),verbose_name="Area of Working", default= '0')
    level = models.IntegerField(choices = levels)
    def __str__ (self):
        return self.name

class index_images(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title to be displayed on Index Page", null=True, blank=True)
    description = models.CharField(max_length=200, verbose_name="short description to be added", null=True, blank=True)
    images = models.ImageField(verbose_name="images to be displayed on index page")
    def __str__(self):
        return self.title


class news(models.Model):
    title = models.CharField(max_length= 200, verbose_name="Heading of the News Clipping")
    paper = models.CharField(max_length= 100, verbose_name="Name of the Newspaper in which the Article was posted")
    date = models.DateField(verbose_name="Date of the News Publishing", null = True, blank = True)
    url = models.URLField(max_length=500, verbose_name="URL of the paper", null =True, blank = True)
    def __str__(self):
        return self.title

class writeup(models.Model):
    question = models.CharField(max_length=100, verbose_name="Question that is to be answered")
    answer = RichTextField(verbose_name = "Answer to the question")
    def __str__(self):
        return self.question

class publication(models.Model):
    title = models.CharField(max_length=500, verbose_name="Title of the paper")
    date = models.DateField(verbose_name="Date of publication")
    DOI = models.CharField(max_length=100, verbose_name="DOI")
