from rest_framework import permissions

class IsInstructorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view): # type: ignore
        # 1. First check: Is the user even logged in?
        if not (request.user and request.user.is_authenticated):
            return False
        
        # 2. Anyone authenticated can see (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 3. Only Admins/Instructors can Create/Edit/Delete
        # We use getattr() as a safer alternative to hassattr + access
        user_role = getattr(request.user, 'role', None)

        return request.user.is_staff or user_role in ['ADMIN', 'INSTRUCTOR']