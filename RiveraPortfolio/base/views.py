from django.shortcuts import render

# Create your views here.

def home(request):
    data = [
        {"title": "Projects", "count": 4},
        {"title": "Skills", "count": 5},
        {"title": "Dean's Listers", "count": 8},
    ]
    # Pass the data to the template
    return render(request, 'base/home.html', {'data': data})
