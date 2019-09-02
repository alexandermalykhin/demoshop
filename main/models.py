from django.db import models

# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    longname = models.TextField()
    



    def __str__(self):
        return self.name