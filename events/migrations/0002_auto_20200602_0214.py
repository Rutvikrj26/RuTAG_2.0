# Generated by Django 3.1a1 on 2020-06-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Event_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Event Date & time'),
        ),
    ]
