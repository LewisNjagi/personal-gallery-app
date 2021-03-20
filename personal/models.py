from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name