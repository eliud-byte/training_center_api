from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit/create objects.
    Students and guests can only view (GET).
    """
    def has_permission(self, request, view) -> bool:  # type: ignore[override]
        # Allow any safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is logged in (not an AnonymousUser)
        if not (request.user and request.user.is_authenticated):
            return False
        
        # Explicitly check for the ADMIN role or staff status
        # Using getattr handles cases where 'role' might not exist on the user object
        user_role = getattr(request.user, 'role', None)

        return request.user.is_staff or user_role == 'ADMIN'