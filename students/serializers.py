from rest_framework import serializers
from .models import Enrollment

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
        read_only_fields = ['created_at'] # Users can't fake the timestamp