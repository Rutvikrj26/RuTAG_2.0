# Generated by Django 3.1a1 on 2020-06-01 16:26

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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer', models.CharField(max_length=50, verbose_name='Organizer')),
                ('location', models.CharField(max_length=100, verbose_name='Location where the event was held')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Enter the Event Details Here')),
                ('Event_date', models.DateTimeField(verbose_name='Event Date & time')),
                ('Event_poster', models.FileField(blank=True, null=True, upload_to='', verbose_name='Add Photo to Event')),
                ('Event_type', models.CharField(choices=[('0', 'Core Group Meeting'), ('1', 'Club Meeting'), ('2', 'Workshop'), ('3', 'Staff & PI Meetings'), ('4', 'Other Events')], max_length=50)),
                ('Event_report', models.FileField(blank=True, null=True, upload_to='', verbose_name='Enter a combined document here')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Writer')),
            ],
            options={
                'ordering': ['-Event_date', '-Event_type'],
            },
        ),
    ]
