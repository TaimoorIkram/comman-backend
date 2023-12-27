from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Organization, Role, Team, Employee, SalaryInvoice, Task, TaskTeam, TaskDuty
from .serializers import OrganizationSerializer, RoleSerializer, TeamSerializer, EmployeeSerializer, SalaryInvoiceSerializer, TaskSerializer, TaskTeamSerializer, TaskDutySerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdmin, IsManager, IsEmployee, IsOwner
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.
# app views
def home(request):
    members = Employee.objects.all()

    return render(request, 'html/dash_team.html', context={'members' : members})

# api views
class OrganizationsView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    ordering_fields = ['name', 'date_created']
    authentication_classes = [JWTAuthentication]
    search_fields = ['name', 'owner__username']
    permission_classes = [IsAuthenticated, IsAdmin]

class OrganizationView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    ordering_fields = ['name', 'date_created']
    authentication_classes = [JWTAuthentication]
    search_fields = ['name', 'owner__username']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated, IsOwner]
        
        return [permission() for permission in permission_classes]


class RolesView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    ordering_fields = ['name']
    authentication_classes = [JWTAuthentication]
    search_fields = ['name']
    permission_classes = [IsAuthenticated, IsAdmin]

class RoleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    ordering_fields = ['name']
    authentication_classes = [JWTAuthentication]
    search_fields = ['name']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated, IsAdmin]
        
        return [permission() for permission in permission_classes]

class TeamsView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    ordering_fields = ['organization__name', 'name']
    authentication_classes = [JWTAuthentication]
    search_fields = ['organization__name', 'name']
    permission_classes = [IsAuthenticated, IsAdmin]

class TeamView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    ordering_fields = ['organization__name', 'name']
    authentication_classes = [JWTAuthentication]
    search_fields = ['organization__name', 'name']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated, IsAdmin]
        
        return [permission() for permission in permission_classes]

class EmployeesView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    ordering_fields = ['organization__name', 'user__username']
    authentication_classes = [JWTAuthentication]
    search_fields = ['organization__name', 'user__username']
    permission_classes = [IsAuthenticated]


class EmployeeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    ordering_fields = ['organization__name', 'user__username']
    authentication_classes = [JWTAuthentication]
    search_fields = ['organization__name', 'user__username']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated, IsAdmin]
        
        return [permission() for permission in permission_classes]

class SalaryInvoicesView(generics.ListCreateAPIView):
    queryset = SalaryInvoice.objects.all()
    serializer_class = SalaryInvoiceSerializer
    ordering_fields = ['date__due', 'payment_status']
    authentication_classes = [JWTAuthentication]
    search_fields = ['employee__name', 'due_date']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]

class SalaryInvoiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaryInvoice.objects.all()
    serializer_class = SalaryInvoiceSerializer
    ordering_fields = ['date__due', 'payment_status']
    authentication_classes = [JWTAuthentication]
    search_fields = ['employee__name', 'due_date']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]

class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    ordering_fields = ['completion_status', 'date_due']
    authentication_classes = [JWTAuthentication]
    search_fields = ['completion_status', 'date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class TaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    ordering_fields = ['completion_status', 'date_due']
    authentication_classes = [JWTAuthentication]
    search_fields = ['completion_status', 'date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class TasksTeamView(generics.ListCreateAPIView): 
    queryset = TaskTeam.objects.all()
    serializer_class = TaskTeamSerializer
    ordering_fields = ['completion_status', 'date_due']
    authentication_classes = [JWTAuthentication]
    search_fields = ['completion_status', 'date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class TaskTeamView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = TaskTeam.objects.all()
    serializer_class = TaskTeamSerializer
    ordering_fields = ['completion_status', 'date_due']
    authentication_classes = [JWTAuthentication]
    search_fields = ['completion_status', 'date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class TaskDutiesView(generics.ListCreateAPIView): 
    queryset = TaskDuty.objects.all()
    serializer_class = TaskDutySerializer
    ordering_fields = ['task__completion_status', 'task__date_due']
    authentication_classes = [JWTAuthentication]
    search_fields = ['task__completion_status', 'task__date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class TaskDutyView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = TaskDuty.objects.all()
    serializer_class = TaskDutySerializer
    ordering_fields = ['task__completion_status', 'task__date_due']
    authentication_classes = [JWTAuthentication]
    search_fields = ['task__completion_status', 'task__date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        user_serialized = UserSerializer(user)
        return Response(user_serialized.data)

class CompanyEmployeesView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, pk, *args, **kwargs):
        employees_from_company = Employee.objects.filter(organization__id=pk)
        employees_from_company_serialized = EmployeeSerializer(employees_from_company, many=True)
        return Response(employees_from_company_serialized.data)
    
class TeamTasksView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, pk, *args, **kwargs):
        employees_from_company = TaskTeam.objects.filter(team__id=pk)
        employees_from_company_serialized = TaskTeamSerializer(employees_from_company, many=True)
        return Response(employees_from_company_serialized.data)
    
class EmployeeOrganizationsView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        employee_in = Employee.objects.filter(user__id=user.id)
        organizations = []
        if len(employee_in) > 0:
            for employee in employee_in:
                organizations.append(Organization.objects.get(id=employee.organization.id))
            
        organizations_serialzed = OrganizationSerializer(organizations, many=True)
        return Response(organizations_serialzed.data)

class UserOrganizationsView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        user_orgs = Organization.objects.filter(owner__id=user.id)    
        organizations_serialzed = OrganizationSerializer(user_orgs, many=True)
        return Response(organizations_serialzed.data)
    
class EmployeeTasksView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, pk, *args, **kwargs):
        user = self.request.user
        organization = Organization.objects.get(id=pk)
        employees = Employee.objects.filter(user__id=user.id)
        duties = []
        if len(employees) > 0:
            for employee in employees:
                duties += TaskDuty.objects.filter(employee__id=employee.id, task__organization__id = organization.id)
        
        duties_serialized = TaskDutySerializer(duties, many=True)
        return Response(duties_serialized.data)