from rest_framework import generics
from .models import Course, CourseInstance
from rest_framework import serializers
from .serializers import CourseSerializer, CourseInstanceSerializer
from rest_framework.exceptions import NotFound


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseInstanceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        return CourseInstance.objects.all()

    def perform_create(self, serializer):
        course_title = self.request.data.get('course_title')
        if course_title:
            try:
                course = Course.objects.get(title=course_title)
            except Course.DoesNotExist:
                raise serializers.ValidationError({"course_title": "Course with this title does not exist."})
            serializer.save(course=course)
        else:
            raise serializers.ValidationError({"course_title": "This field is required."})

class CourseInstanceDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        course_id = self.kwargs['course_id']
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        print(f"Deleting instance with Course ID: {course_id}, Year: {year}, Semester: {semester}")
        try:
            return CourseInstance.objects.get(
                course_id=course_id,
                year=year,
                semester=semester
            )
        except CourseInstance.DoesNotExist:
            raise NotFound(detail="CourseInstance matching query does not exist.", code=404)
    
class AllCourseInstancesAPIView(generics.ListAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer
