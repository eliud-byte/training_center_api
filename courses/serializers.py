from rest_framework import serializers
from .models import Course, Cohort

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = '__all__'