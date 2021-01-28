from django.urls import path
from .views import TeacherList, StudentList, ProfileDetail, UserCreate, LoginView

urlpatterns = [
    path("teachers/", TeacherList.as_view(), name="teacher_list"),
    path("students/", StudentList.as_view(), name="student_list"),
    path("profile/<int:pk>/", ProfileDetail.as_view(), name="profile_detail"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login")
]