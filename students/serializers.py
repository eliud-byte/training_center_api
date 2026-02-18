from rest_framework import serializers
from .models import Enrollment, Grade

class GradeSerializer(serializers.ModelSerializer):
    # These should be read_only because they are just for display
    student_name = serializers.ReadOnlyField(source='enrollment.student.username')
    cohort_name = serializers.ReadOnlyField(source='enrollment.cohort.name')

    class Meta:
        model = Grade
        fields = ['id', 'enrollment', 'student_name', 'cohort_name', 'score', 'feedback', 'graded_at']
        read_only_fields = ['graded_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.username')
    cohort_name = serializers.ReadOnlyField(source='cohort.name')

    # This is the magic line
    grade = GradeSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            'id',
            'student',
            'student_name',
            'cohort',
            'cohort_name',
            'status',
            'grade',
            'created_at',
        ]
        read_only_fields = ['created_at', 'student'] # Users can't fake the timestamp