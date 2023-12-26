from rest_framework.permissions import BasePermission
from .models import Organization

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Admin').exists():
            return True
        return False

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Employee').exists():
            return True
        return False

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Employee').exists():
            return True
        return False

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        organization_id = request.path_info.split('/')[-2]
        organization = Organization.objects.filter(owner__id=request.user.id)
        if organization:
            if organization[0].id == int(organization_id): return True
        return False