# Generated by Django 2.2 on 2019-08-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_remove_job_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='challenge',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='job',
            name='team',
            field=models.CharField(max_length=200),
        ),
    ]
