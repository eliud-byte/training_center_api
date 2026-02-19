from django.contrib import admin
from .models import Enrollment, Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    # This displays grades on the admin panel
    list_display = ('get_student', 'get_cohort', 'score', 'graded_at')

    # This adds a search bar to find grades by student name quickly
    search_fields = ('enrollment__student__username', 'enrollment__cohort__name')

    # Helper methods to "reach into the Enrollment model for display"
    @admin.display(ordering='enrollment__student', description='Student')
    def get_student(self, obj):
        return obj.enrollment.student.username
    
    @admin.display(ordering='enrollment__cohort', description='Cohort')
    def get_cohort(self, obj):
        return obj.enrollment.cohort.name
    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'cohort', 'status', 'created_at')
    list_filter = ('status', 'cohort')

