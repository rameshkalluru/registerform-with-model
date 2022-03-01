import email
from django.db import models

# Create your models here.
class ram(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    password=models.IntegerField()
    repassword=models.IntegerField()
    email=models.EmailField()
    url=models.URLField()
    image=models.ImageField()
    file=models.FileField()
    li=[['MALE','MALE'],['FEMALE','FEMALE']]
    gender=models.CharField(choices=li,max_length=10)
    dob=models.DateField()
