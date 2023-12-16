from django.db import models
from hrm.models import Member

# default models for storing basic data
class ActivityType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class CustomerStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class ApplicationStatusType(models.Model): pass

# Create your models here.
class Customer(models.Model): 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    visit_date = models.DateField(auto_now=True)
    employee = models.ForeignKey(Member, null=True, on_delete=models.PROTECT)
    # contact_number = models.IntegerField(default=0) # format: 9230765001234 (PK), 15555550100 (USA)
    

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class Feedback(models.Model):
    heading = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    rating = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.comment[:25] + '...'

class Task(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    due_date = models.DateField(null=True)
    completion = models.BooleanField(default=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' due ' + self.due_date.ctime()
    
class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_status = models.BooleanField()
    arrears = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return str(self.due_amount) + ' due ' + self.due_date.ctime()
    
class Services(models.Model): pass

class Activity(models.Model):
    type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)

    def __str__(self) -> str:
        return '[' + self.type.name + ']' + ' ' + self.message