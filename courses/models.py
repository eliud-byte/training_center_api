from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    syllabus = models.TextField(help_text="Outline of the course modules")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Cohort(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE,
        related_name='cohorts'
    )
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # If instructor is fired, don't delete the class history
        null=True,
        blank=True,
        related_name='assigned_cohorts',
        limit_choices_to={'role': 'INSTRUCTOR'} #Only show Instructors in dropdowns
    )
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.PositiveIntegerField(default=20)

    def clean(self):
        # Optional: Validation to ensure end_date is after start_date
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date.")
        
    def __str__(self):
        return self.name

