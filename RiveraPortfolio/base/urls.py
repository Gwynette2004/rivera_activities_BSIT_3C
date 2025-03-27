from django.urls import path
from . import views
from .views import (
    StudentListCreateView,
    StudentDetailView,
    StudentDeleteView,
    StudentUpdateView
)

urlpatterns = [
    path('', views.home, name="home"),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
]
