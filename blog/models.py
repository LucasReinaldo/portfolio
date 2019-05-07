from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    # Troca o nome do title em /admin para o nome do title do post.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200] + '[...]'

