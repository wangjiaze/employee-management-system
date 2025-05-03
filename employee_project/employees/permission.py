
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.profile.role == 'admin'

class IsHRUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.profile.role in ['admin', 'hr']

class IsEmployeeUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.profile.role in ['admin', 'hr', 'employee']