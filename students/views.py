from typing import TYPE_CHECKING, cast
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from django.db.models import QuerySet
from .models import Enrollment, Grade
from .serializers import EnrollmentSerializer, GradeSerializer
from django.contrib.auth import get_user_model
from .permissions import IsInstructorOrAdmin

User = get_user_model()

if TYPE_CHECKING:
    from users.models import User as UserType

class EnrollmentViewSet(viewsets.ModelViewSet):
    # Provide a base queryset so some DRF helpers and tools work
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated] # Only logged in users can access
    
    def get_queryset(self):  # type: ignore[override]
        # 1. If Admin/Instructor, show ALL enrollments
        user = cast("UserType", self.request.user)
        if user.is_staff or (hasattr(user, 'role') and user.role in ['ADMIN', 'INSTRUCTOR']):
            return Enrollment.objects.all()
        
        # 2. If Student, show ONLY their own enrollments
        return Enrollment.objects.filter(student=user)

    def perform_create(self, serializer):
        # Automatically set the 'student' field to the currently logged-in user
        # This prevents students from enrolling others.

        # Optional: specific check to ensure Instructors don't enroll themselves as students
        user = cast("UserType", self.request.user)
        if getattr(user, 'role', None) == 'INSTRUCTOR':
            raise ValidationError("Instructors cannot enroll in courses")
        
        serializer.save(student=self.request.user)

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsInstructorOrAdmin]

    def get_queryset(self): # type: ignore
        user = self.request.user
        # If not authenticated (AnonymousUser), return empty queryset
        if not getattr(user, 'is_authenticated', False):
            return Grade.objects.none()
        # Admins and Instructors see all grades
        if user.is_staff or getattr(user, 'role', None) in ['ADMIN', 'INSTRUCTOR']:
            return Grade.objects.all()
        # Students see only their own grades
        return Grade.objects.filter(enrollment__student=user)