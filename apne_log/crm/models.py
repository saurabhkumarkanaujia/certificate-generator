from django.db import models

# Create your models here.

class Certificate(models.Model):
    name=models.CharField(max_length=245)
    college=models.CharField(max_length=245)
    dept_name=models.CharField(max_length=245)
    start=models.CharField(max_length=245)
    end=models.CharField(max_length=245)