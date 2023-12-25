from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Employee').exists():
            return True
        return False