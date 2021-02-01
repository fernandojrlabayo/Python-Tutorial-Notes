from django.db import models

# Create your models here.

class Employee(models.Model):

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Reason = models.CharField(max_length=400)
    teamLeader = models.CharField(max_length=100)

    