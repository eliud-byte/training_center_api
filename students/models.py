from django.db import models
from django.conf import settings
from courses.models import Cohort

class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'pending'),
        ('ACTIVE', 'active'),
        ('COMPLETED', 'completed'),
        ('DROPPED', 'dropped'),
    )

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='enrollments',
        limit_choices_to={'role': 'STUDENTS'} # Only students can enroll
    )

    cohort = models.ForeignKey(
        Cohort,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'cohort'] # Prevents double-booking

    def __str__(self):
        return f"{self.student} --> {self.cohort}"
