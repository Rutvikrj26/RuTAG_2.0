from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="name of the person contacting")
    email = models.EmailField(verbose_name="email of the person contacting")
    query = models.CharField(max_length=1000, verbose_name="Query of the person")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date & Time of Querying")


positions = (('0','RuTAG Club - trainee'), ('1','RuTAG Club - Project Member'), ('2', 'RuTAG Club - Project Leader'),
             ('3', 'RuTAG Club - Club Coordinator'),('4', 'RuTAG Club - Club principal'),('5', 'RuTAG Club - Club Secratary'),
             ('6', 'Core - Jr. Project Assistant'), ('7', 'Core - Sr. Project Assistant'), ('8', 'Core - Club Principal Inspector'), ('9', 'Core - Chairman'), ('10', 'Core - PI'),
             ('11', 'Core - Jr. Project Attendant'), ('12','Core - Project Associate'), ('13', 'Core - Coordinator and Principal Investigator (PI)'), ('14', 'Core - Chairman, Core Group'),('15', 'Core - Web Developer'), ('16','Research Scholar'))

levels = [(i,i) for i in range(8)]

class Member(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name of the Member")
    position = models.CharField(max_length=50, choices=positions, verbose_name="position of the member")
    image = models.ImageField(verbose_name="Profile Picture of the Member", default='/static/default.jpg')
    detail = models.TextField(verbose_name="Some detail about the Member", null=True,blank=True)
    email = models.EmailField(verbose_name="email id of the member", default="rutagiitd@gmail.com")
    work = models.CharField(max_length=20, choices=(('0', 'Core'), ('1', 'Club')),verbose_name="Area of Working", default= '0')
    level = models.IntegerField(choices = levels)
    def __str__ (self):
        return self.name


