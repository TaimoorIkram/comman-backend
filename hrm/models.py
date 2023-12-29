from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Team(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE) 
    team_lead = models.ForeignKey('Employee', on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.organization.name + ' - ' + self.name

class Employee(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.ForeignKey(Role, on_delete=models.PROTECT)
    primary_team = models.ForeignKey(Team, on_delete=models.PROTECT, null=True, blank=True)
    contact_number = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username + ', ' + self.rank.name + ' at ' + self.organization.name

class SalaryInvoice(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    due_amount = models.BigIntegerField()
    date_issued = models.DateTimeField(auto_now=True)
    date_due = models.DateTimeField(null=True)
    payment_status = models.BooleanField()
    arrears = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self) -> str:
        return self.employee.user.username + ' ' + self.due_amount + ' ' + self.payment_status 
    
class Task(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    completion_status = models.BooleanField()
    details = models.CharField(max_length=1000)
    date_due = models.DateField()

    def __str__(self) -> str:
        return self.title + ' ' + str(self.date_due) + ' ' + str(self.completion_status)

class TaskTeam(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    responsibility = models.TextField()

    def __str__(self) -> str:
        return self.team.name + ' - ' + self.responsibility

class TaskDuty(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    details = models.TextField()
    date_due = models.DateField()
    completion_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.employee.user.username + ' - ' + self.task.title + ' - ' + self.details

class Message(models.Model): pass