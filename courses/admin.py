from django.contrib import admin
from .models import Course, Cohort

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title',)

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'instructor', 'start_date', 'capacity')
    list_filter = ('start_date', 'course')
    search_fields = ('name', 'course__title')