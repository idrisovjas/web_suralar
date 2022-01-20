from django.db import models


# Create your models here.
class post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()


    def __str__(self):
        return self.title



