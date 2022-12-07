from django.db import models

# Create your models here.
class SampleImage(models.Model):
    sample = models.ImageField(upload_to = "images")