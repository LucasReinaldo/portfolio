from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    votes = models.IntegerField(default = 1)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default='')


    # Troca o nome do title em /admin para o nome do title do post.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200] + '[...]'

