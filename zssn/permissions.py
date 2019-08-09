from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True


class CantUpdate(BasePermission):
    def has_permission(self, request, view):
        if not request.method in ['PUT', 'PATCH']:
            return True


class CantDelete(BasePermission):
    def has_permission(self, request, view):
        if request.method != 'DELETE':
            return True
