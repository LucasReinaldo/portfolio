# Generated by Django 2.2 on 2019-05-29 18:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190529_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]