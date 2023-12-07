from django.db import models
from hrm.models import Member

# default models for storing basic data
class ActivityType(models.Model):
    name = models.CharField(max_length=30)

class CustomerType(models.Model): pass
class ApplicationStatusType(models.Model): pass

# Create your models here.
class Customer(models.Model): 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    visit_date = models.DateField(auto_now=True)
    employee = models.ForeignKey(Member, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class Feedback(models.Model): pass
class Task(models.Model): pass
class Activity(models.Model):
    type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)

    def __str__(self) -> str:
        return '[' + self.type.name + ']' + ' ' + self.message