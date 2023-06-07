from django.urls import path
from .views import (
    UserSignUpView,
    ForgotPasswordView,
    StudentListView,
    StudentDetailView,
    TeacherStudentListView,
    AdminUserListView,
)

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('teacher/students/', TeacherStudentListView.as_view(), name='teacher-student-list'),
    path('admin/users/', AdminUserListView.as_view(), name='admin-user-list'),
]
