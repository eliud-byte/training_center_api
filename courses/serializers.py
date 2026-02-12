from rest_framework import serializers
from .models import Course, Cohort

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CohortSerializer(serializers.ModelSerializer):
    # These fields are "Read Only" - they appear in GET responses but aren't required for POST
    course_name = serializers.ReadOnlyField(source='course.title')
    instructor_name = serializers.ReadOnlyField(source='instructor.username')

    class Meta:
        model = Cohort
        fields = [
            'id',
            'name',
            'course',
            'course_name',  # <--- distinct field for the name
            'instructor',
            'instructor_name',  # <--- distinct field for the username
            'start_date',
            'end_date',
            'capacity',
        ]
