from django.contrib import admin
from .models import Activity, Customer, ActivityType, Feedback, CustomerTask, CustomerStatus, Bill

# deafult models for types
admin.site.register(ActivityType)
admin.site.register(CustomerStatus)

# Register your models here.
admin.site.register(Customer)
admin.site.register(Feedback)
admin.site.register(CustomerTask)
admin.site.register(Bill)
admin.site.register(Activity)