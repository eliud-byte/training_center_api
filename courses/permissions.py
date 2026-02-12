from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit/create objects.
    Students and guests can only view (GET).
    """
    def has_permission(self, request, view):
        # Allow any safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the admin
        return request.user and request.user.is_staff or (
            hasattr(request.user, 'role') and request.user.role == 'ADMIN'
        )