from django.urls import path
from . import views
from .views import ItemListCreateView, ItemDetailView, ItemDeleteView, ItemUpdateView


urlpatterns = [
    path('',views.home, name="home"),
    path('items/', ItemListCreateView.as_view(),name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/update/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),
    path('items/delete/<int:pk>/', ItemDeleteView.as_view(), name='item-delete'),
]