from rest_framework import serializers
from .models import Enrollment, Grade

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.username')
    cohort_name = serializers.ReadOnlyField(source='cohort.name')

    class Meta:
        model = Enrollment
        fields = [
            'id',
            'student',
            'student_name',
            'cohort',
            'cohort_name',
            'status',
            'created_at',
        ]
        read_only_fields = ['created_at', 'student'] # Users can't fake the timestamp

class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='enrollment.student.username')
    cohort_name = serializers.ReadOnlyField(source='enrollment.cohort.name')

    class Meta:
        model = Grade
        fields = ['id', 'enrollment', 'student_name', 'cohort_name', 'score', 'feedback', 'graded_at']