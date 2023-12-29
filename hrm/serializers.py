from rest_framework import serializers
from .models import Organization, Team, Role, Employee, SalaryInvoice, Task, TaskTeam, TaskDuty
from django.contrib.auth.models import User, Group
from rest_framework.validators import UniqueValidator

# write your serializers here
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(
        write_only=True, required=True)
    password_confirmation = serializers.CharField(
        write_only=True, required=True)
  
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_confirmation', 'email', 'first_name', 'last_name', 'groups')
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class OrganizationSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.IntegerField(write_only=True)

    name = serializers.CharField(
        required=True, 
        validators=[UniqueValidator(queryset=Organization.objects.all())]
    )

    class Meta:
        model = Organization
        fields = '__all__'
        depth = 1

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1

class TaskSerializer(serializers.ModelSerializer):
    # organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.IntegerField(write_only=True)

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
    employee_id = serializers.IntegerField(write_only=True)
    employee = EmployeeSerializer(read_only=True)
    
    task_id = serializers.IntegerField(write_only=True)
    task = TaskSerializer(read_only=True)

    class Meta:
        model = TaskDuty
        fields = '__all__'
        depth = 1