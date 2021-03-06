from django.db import models
from ckeditor.fields import RichTextField

class organization(models.Model):
    name = models.CharField(max_length=500, verbose_name="Name")
    contact = models.CharField(max_length=200,verbose_name= "Person of Contact")
    email = models.EmailField(verbose_name="POC's Email id")
    type = models.CharField(max_length=50,choices=(('0', 'NGO'), ('1', 'Government Organizations'), ('2', 'Colleges')))
    description = RichTextField()
    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Writer")
    organization = models.ForeignKey(organization,max_length=200,on_delete=models.CASCADE,verbose_name = "Associated Organization", null=True, blank=True)
    title = models.CharField(max_length = 50,verbose_name = "Title")
    short = models.CharField(max_length=200, verbose_name="Short Description")
    content = RichTextField(verbose_name="Enter the Product description & extra photos over here")
    Product_image = models.ImageField(verbose_name="Product Picture")
    def __str__(self):
        return self.title

class product_image(models.Model):
    Product_image = models.ImageField(verbose_name="Enter one Product image")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
