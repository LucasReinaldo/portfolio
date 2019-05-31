# Generated by Django 2.2 on 2019-05-30 13:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_imagetext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='imageText',
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True),
        ),
    ]