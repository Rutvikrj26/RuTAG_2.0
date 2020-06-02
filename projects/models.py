from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class professor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    department = models.CharField(max_length = 50, verbose_name='Expertise of Professor')
    email = models.EmailField(verbose_name='Email id')
    profilepic = models.ImageField(verbose_name='Picture to be displayed on Website',null=True,blank=True)
    def __str__(self):
        return self.name


positions = (('1', 'undergrad 1st-year'),('2','undergrad 2nd-year'),('3','undergrad 3rd-year'),('4','undergrad 4th-year'),('5','Masters 1st-year'),('6','Masters 2nd-year'), ('7','pHD'))
statuses = (('1', 'Proposed'),('2','in Pipeline'),('3','completed'), ('4','Executed'))
Club_Membership = (('0', 'Yes'),('1', 'No'))

class student(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    department = models.CharField(max_length=50,verbose_name='Department of Student')
    email = models.EmailField(verbose_name='Email id')
    position = models.CharField(max_length=50,choices=positions)
    member = models.CharField(max_length=50, choices=Club_Membership)
    profilepic = models.ImageField(verbose_name='Picture to be displayed on Website',null=True, blank=True)
    def __str__(self):
        return self.name

class engineer(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    position = models.CharField(max_length=50, verbose_name='Position of the Engineer')
    email = models.EmailField(verbose_name='Email id')
    profilepic = models.ImageField(verbose_name='Picture to be displayed on Website',null=True, blank=True)
    def __str__(self):
        return self.name



class Project(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Writer")
    professor = models.CharField(max_length=200,verbose_name = "professors")
    student = models.CharField(max_length=200,verbose_name= "students")
    engineer = models.CharField(max_length=200, verbose_name="engineers")
    title = models.CharField(max_length = 500,verbose_name = "Title")
    content = RichTextField(verbose_name="Enter the Project proposal/Abstract over here")
    status = models.CharField(max_length=50,choices=statuses)
    Project_date = models.DateField(verbose_name="Project Starting Date", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-Project_date']

class Projectreports(models.Model):
    Project_report = models.FileField(verbose_name='Project Reports',null=True, blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True)


