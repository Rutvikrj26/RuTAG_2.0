# Generated by Django 3.1a1 on 2020-06-04 04:53

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
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('contact', models.CharField(max_length=200, verbose_name='Person of Contact')),
                ('email', models.EmailField(max_length=254, verbose_name="POC's Email id")),
                ('type', models.CharField(choices=[('0', 'NGO'), ('1', 'Government Organizations'), ('2', 'Colleges')], max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('short', models.CharField(max_length=200, verbose_name='Short Description')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Enter the Product description & extra photos over here')),
                ('Product_image', models.ImageField(upload_to='', verbose_name='Product Picture')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Writer')),
                ('organization', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.organization', verbose_name='Associated Organization')),
            ],
        ),
        migrations.CreateModel(
            name='product_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_image', models.ImageField(upload_to='', verbose_name='Enter one Product image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
