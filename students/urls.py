from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrollmentViewSet, GradeViewSet

router = DefaultRouter()
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'grades', GradeViewSet, basename='grade')

urlpatterns = [
    path('', include(router.urls)),
]

