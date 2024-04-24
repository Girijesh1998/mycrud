from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.IntegerField(unique=True, primary_key=True ,verbose_name="Id")
    fname = models.CharField(max_length=70 ,verbose_name="First Name")
    lname = models.CharField(max_length=70 ,verbose_name="Last Name")
    roll  = models.IntegerField(unique=True ,verbose_name="Roll")
    mobile= models.CharField(max_length=12 , verbose_name="Mobile")
    email = models.EmailField(verbose_name="Email Id")