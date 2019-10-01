from django.db import models

# Create your models here.
GENDER=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')

)
class Students(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=10)
    address=models.TextField()
    course=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=GENDER,default='M')
class faculity(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=10)
    address=models.TextField()
    dept=models.CharField(max_length=50)  