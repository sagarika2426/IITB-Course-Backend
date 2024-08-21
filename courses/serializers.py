from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'course_code', 'description']

class CourseInstanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = CourseInstance
        fields = ['id', 'course', 'year', 'semester']
