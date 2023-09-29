from rest_framework import serializers
from django.conf import settings
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        if len(data['students']) > settings.MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError('Max count of students is 20')
        if self.instance and self.instance.students.count() > settings.MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError('Max count of OPEN ads')
        return data
