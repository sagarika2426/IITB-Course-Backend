from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'course_code', 'description']

class CourseInstanceSerializer(serializers.ModelSerializer):
    # course_title = serializers.CharField(write_only=True)
    course_id = serializers.IntegerField(source='course.id', write_only=True)  # Add this field
    course = serializers.SerializerMethodField()

    class Meta:
        model = CourseInstance
        fields = ['id', 'course', 'course_id', 'year', 'semester']

    def get_course(self, obj):
        if obj.course:
            return {
                'id': obj.course.id,
                'title': obj.course.title,
                'course_code': obj.course.course_code,
                'description': obj.course.description
            }
        return None

    def create(self, validated_data):
        course_title = validated_data.pop('course_id')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise serializers.ValidationError({"course_id": "Course with this ID does not exist."})
        
        # Pass `course` directly to `create` method
        instance = CourseInstance.objects.create(course=course, year=validated_data['year'], semester=validated_data['semester'])
        return instance

