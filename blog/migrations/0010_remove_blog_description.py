# Generated by Django 2.2 on 2019-06-03 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190531_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
    ]
