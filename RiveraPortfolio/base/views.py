from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializer import ItemSerializer
# Create your views here.

def home(request):
    data = [
        {"title": "Projects", "count": 4},
        {"title": "Skills", "count": 5},
        {"title": "Dean's Listers", "count": 8},
    ]
    # Pass the data to the template
    return render(request, 'base/home.html', {'data': data})


# get all items and create a new item in one
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#get one item
class ItemDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#update an item
class ItemUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#delete an item
class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer