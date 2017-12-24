from django.db import models

# Create your models here.
class Output(models.Model):
    img1 = models.FileField(upload_to='img')
    img2 = models.FileField(upload_to='img')