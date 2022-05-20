from django.db import models
from django.forms import FileField
class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_des=models.TextField()
    service_image =models.FileField(upload_to="services/",max_length=250,null=True,default=None)


# Create your models here.
