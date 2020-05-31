# Generated by Django 3.1a1 on 2020-05-30 14:00

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='engineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="student's name")),
                ('position', models.CharField(max_length=50, verbose_name='Position of the Engineer')),
                ('email', models.EmailField(max_length=254, verbose_name='Email id')),
            ],
        ),
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Professor_name')),
                ('department', models.CharField(max_length=50, verbose_name='Expertise of Professor')),
                ('email', models.EmailField(max_length=254, verbose_name='Email id')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="student's name")),
                ('department', models.CharField(max_length=50, verbose_name='Department of Student')),
                ('email', models.EmailField(max_length=254, verbose_name='Email id')),
                ('position', models.CharField(choices=[('1', 'undergrad 1st-year'), ('2', 'undergrad 2nd-year'), ('3', 'undergrad 3rd-year'), ('4', 'undergrad 4th-year'), ('5', 'Masters 1st-year'), ('6', 'Masters 2nd-year'), ('7', 'pHD')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Enter the Project proposal over here')),
                ('Project_poster', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Add Photo to product')),
                ('Project_report', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Add Report of project')),
                ('status', models.CharField(choices=[('1', 'Proposed'), ('2', 'in Pipeline'), ('3', 'completed'), ('4', 'Executed')], max_length=50)),
                ('Project_date', models.DateTimeField(verbose_name='Project Starting Date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Writer')),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.engineer', verbose_name='engineers')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.professor', verbose_name='professors')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.student', verbose_name='students')),
            ],
            options={
                'ordering': ['-Project_date'],
            },
        ),
    ]
