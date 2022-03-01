from django.db import models

# Create your models here.
# class man(models.Model):
#     god=models.CharField(max_length=20)
#     angle=models.CharField(max_length=20)
#     phone=models.BigIntegerField()
#     li=[['MALE','Male'],['FEMALE','Female']]
#     gender=models.CharField(max_length=10, choices=li)
    

class registermodel(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    dob=models.DateField()
    li=[['MALE','Male'],['FEMALE','Female']]
    gender=models.CharField(max_length=10, choices=li)
        