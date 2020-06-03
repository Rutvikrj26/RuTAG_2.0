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
statuses = (('0', 'Proposed'),('1','in Pipeline'),('2','completed'), ('3','Executed'))
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
    professor = models.CharField(max_length=200,verbose_name = "professors", null=True, blank=True)
    student = models.CharField(max_length=200,verbose_name= "students", null=True, blank=True)
    engineer = models.CharField(max_length=200, verbose_name="engineers", null=True, blank=True)
    title = models.CharField(max_length = 500,verbose_name = "Title")
    content = RichTextField(verbose_name="Enter the Project proposal/Abstract over here", null=True, blank=True)
    status = models.CharField(max_length=50,choices=statuses)
    Project_date = models.DateField(verbose_name="Project Starting Date", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-Project_date']

class project_report(models.Model):
    Project_report = models.FileField(verbose_name="Project Report")
    project = models.ForeignKey( Project ,on_delete=models.CASCADE)


