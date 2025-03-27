from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializer import StudentSerializer

# Home view with sample data
def home(request):
    data = [
        {"title": "Projects", "count": 4},
        {"title": "Skills", "count": 5},
        {"title": "Dean's Listers", "count": 8},
    ]
    return render(request, 'base/home.html', {'data': data})

# Get all students and create a new student
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Get one student
class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Update a student
class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Delete a student
class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
