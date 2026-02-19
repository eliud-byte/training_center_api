from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course, Cohort
from .serializers import CourseSerializer, CohortSerializer
from .permissions import IsAdminOrReadOnly

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

    # Explicitly list which backends this view uses
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Define EXACT match filters
    filterset_fields = ['price']

    # Define TEXT search fields
    search_fields = ['title', 'description']

    # Define which fields can be used for SORTING
    ordering_fields = ['price', 'title']

class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer
    permission_classes = [IsAdminOrReadOnly]