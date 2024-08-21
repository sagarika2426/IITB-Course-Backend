from django.urls import path
from .views import (
    CourseListCreateAPIView, CourseDetailAPIView,
    CourseInstanceListCreateAPIView, CourseInstanceDetailAPIView
)

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListCreateAPIView.as_view(), name='instance-list-create'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', CourseInstanceDetailAPIView.as_view(), name='instance-detail'),
]
