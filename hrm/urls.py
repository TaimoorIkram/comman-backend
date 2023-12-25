from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'hrm'
router = DefaultRouter(trailing_slash=True)

urlpatterns = [
    path('home/', views.home, name='home'),
    path('organizations/', views.OrganizationsView.as_view(), name='organizations'),
    path('organization/<int:pk>/', views.OrganizationView.as_view(), name='organization'),
    path('roles/', views.RolesView.as_view(), name='roles'),
    path('role/<int:pk>/', views.RoleView.as_view(), name='role'),
    path('teams/', views.TeamsView.as_view(), name='teams'),
    path('team/<int:pk>/', views.TeamView.as_view(), name='team'),
    path('employees/', views.EmployeesView.as_view(), name='employees'),
    path('employee/<int:pk>/', views.EmployeeView.as_view(), name='employee'),
    path('invoices/', views.SalaryInvoicesView.as_view(), name='invoices'),
    path('invoice/<int:pk>/', views.SalaryInvoiceView.as_view(), name='invoice'),
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('tasks-team/', views.TasksTeamView.as_view(), name='tasks-team'),
    path('task-team/<int:pk>/', views.TaskTeamView.as_view(), name='task-team'),
    path('duties/', views.TaskDutiesView.as_view(), name='duties'),
    path('duty/<int:pk>/', views.TaskDutyView.as_view(), name='duty'),
] + router.urls