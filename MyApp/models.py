from django.db import models

# Create your models here.
class Task(models.Model):
    Student = models.CharField(max_length=100,null=True,blank=True)
    Batch = models.CharField(max_length=100,null=True,blank=True)
    Tutor = models.CharField(max_length=100,null=True,blank=True)
    Task_title = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(max_length=100,null=True,blank=True)