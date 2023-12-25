from django.contrib import admin
from .models import Employee, Organization, Role, SalaryInvoice, Task, TaskDuty, TaskTeam, Team

# Register your models here.
admin.site.register(Organization)
admin.site.register(Role)
admin.site.register(Team)
admin.site.register(Employee)
admin.site.register(SalaryInvoice)
admin.site.register(Task)
admin.site.register(TaskTeam)
admin.site.register(TaskDuty)