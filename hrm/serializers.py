from rest_framework import serializers
from .models import Organization, Team, Role, Employee, SalaryInvoice, Task, TaskTeam, TaskDuty
from django.contrib.auth.models import User

# write your serializers here
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class OrganizationSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Organization
        fields = '__all__'
        depth = 1

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        depth = 1

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class SalaryInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryInvoice
        fields = '__all__'
        depth = 1

class TaskTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTeam
        fields = '__all__'
        depth = 1

class TaskDutySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDuty
        fields = '__all__'
        depth = 1