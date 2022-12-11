from django.db import models

# Create your models here.


class registeration(models.Model):
    Myname = models.CharField(max_length=39)
    Subject = models.CharField(max_length=40)
    Myurl = models.URLField(max_length=200)
    city = models.CharField(max_length=200)


class mynewform(models.Model):
    Studentname = models.CharField(max_length=33)
    Teachername = models.CharField(max_length=44)
    myclass = models.CharField(max_length=44)
    registraionid = models.BigIntegerField(max_length=44)
