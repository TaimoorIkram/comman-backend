from django.contrib import admin
from .models import Customer, ActivityType, Feedback, Task, CustomerStatus, ApplicationStatusType, Bill

# deafult models for types
admin.site.register(ActivityType)
admin.site.register(CustomerStatus)

# Register your models here.
admin.site.register(Customer)
admin.site.register(Feedback)
admin.site.register(Task)
admin.site.register(Bill)