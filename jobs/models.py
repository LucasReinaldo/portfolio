from django.db import models
from django.utils import timezone

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateField(default=timezone.now)
    site = models.CharField(max_length=100, default='https://')


    def __str__(self):
        return self.title
