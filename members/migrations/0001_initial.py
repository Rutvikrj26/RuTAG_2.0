# Generated by Django 3.1a1 on 2020-06-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name of the person contacting')),
                ('email', models.EmailField(max_length=254, verbose_name='email of the person contacting')),
                ('query', models.CharField(max_length=1000, verbose_name='Query of the person')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date & Time of Querying')),
            ],
        ),
        migrations.CreateModel(
            name='index_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title to be displayed on Index Page')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='short description to be added')),
                ('images', models.ImageField(upload_to='static/img/', verbose_name='images to be displayed on index page')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of the Member')),
                ('position', models.CharField(max_length=50, verbose_name='position of the member')),
                ('image', models.ImageField(default='/static/default.jpg', upload_to='', verbose_name='Profile Picture of the Member')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='Some detail about the Member')),
                ('email', models.EmailField(default='rutagiitd@gmail.com', max_length=254, verbose_name='email id of the member')),
                ('work', models.CharField(choices=[('0', 'Core'), ('1', 'Club')], default='0', max_length=20, verbose_name='Area of Working')),
                ('level', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)])),
            ],
        ),
    ]
