from django.contrib import admin

from students.models import Student
from students.models import Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


# @admin.register(Course)
