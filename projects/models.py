from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class professor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Professor_name")
    department = models.CharField(max_length = 50, verbose_name='Expertise of Professor')
    email = models.EmailField(verbose_name='Email id')
    
positions = (('1', 'undergrad 1st-year'),('2','undergrad 2nd-year'),('3','undergrad 3rd-year'),('4','undergrad 4th-year'),('5','Masters 1st-year'),('6','Masters 2nd-year'), ('7','pHD'))
statuses = (('1', 'Proposed'),('2','in Pipeline'),('3','completed'), ('4','Executed')) 

class student(models.Model):
    name = models.CharField(max_length=50, verbose_name="student's name")
    department = models.CharField(max_length=50,verbose_name='Department of Student')
    email = models.EmailField(verbose_name='Email id')
    position = models.CharField(max_length=50,choices=positions)

class engineer(models.Model):
    name = models.CharField(max_length=50, verbose_name="student's name")
    position = models.CharField(max_length=50, verbose_name='Position of the Engineer')
    email = models.EmailField(verbose_name='Email id')

class Project(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Writer")
    professor = models.ForeignKey(professor,on_delete=models.CASCADE,verbose_name = "professors")
    student = models.ForeignKey(student,on_delete=models.CASCADE,verbose_name= "students")
    engineer = models.ForeignKey(engineer, on_delete=models.CASCADE, verbose_name="engineers")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField(verbose_name="Enter the Project proposal over here")
    Project_poster = models.ImageField(blank = True,null = True,verbose_name="Add Photo to product")
    Project_report = models.ImageField(blank=True, null=True, verbose_name="Add Report of project")
    status = models.CharField(max_length=50,choices=statuses)
    Project_date = models.DateTimeField(verbose_name="Project Starting Date")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-Project_date']

