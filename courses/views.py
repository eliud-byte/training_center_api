from rest_framework import viewsets
from .models import Course, Cohort
from .serializers import CourseSerializer, CohortSerializer
from .permissions import IsAdminOrReadOnly

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer
    permission_classes = [IsAdminOrReadOnly]