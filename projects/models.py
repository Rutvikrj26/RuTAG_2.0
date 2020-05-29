from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class professor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Professor_name")
    department = models.CharField(max_length = 50, verbose_name='Expertise of Professor')
    email = models.EmailField(verbose_name='Email id')
    
positions = ['undergrad 1st-year','undergrad 2nd-year','undergrad 3rd-year','undergrad 4th-year','Masters 1st-year','Masters 2nd-year', 'pHD'  ]

class student(models.Model):
    name = models.CharField(max_length=50, verbose_name="student's name")
    department = models.CharField(max_length=50,verbose_name='Department of Student')
    email = models.EmailField(verbose_name='Email id')
    position = models.CharField(max_length=50, verbose_name='Course the student is Pursuing & year')
    
class Project(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Writer")
    professor = models.ForeignKey(professor,on_delete=models.DO_NOTHING,verbose_name = "professors")
    student = models.ForeignKey(student,on_delete=models.DO_NOTHING,verbose_name= "students")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    Project_date = models.DateTimeField(verbose_name="Project Completion Date")
    Project_poster = models.ImageField(blank = True,null = True,verbose_name="Add Photo to product")
    Project_report = models.ImageField(blank=True, null=True, verbose_name="Add Report of project")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-Project_date']