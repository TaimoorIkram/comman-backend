from django.db import models

# Create your models here.
class Rank(models.Model):
    title = models.CharField(max_length=30)

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)

# default models for storing deafult data
class EmployeeType(models.Model): pass
class PaymentType(models.Model): pass