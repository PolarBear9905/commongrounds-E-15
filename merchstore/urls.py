from django.urls import path
from .views import ProductListView, ProductDetailView
urlpatterns = [
    path('items/', ProductListView.as_view(), name="merchstore-list"),
    path('item/<int:pk>/', ProductDetailView.as_view(), name="merchstore-detail"),
]

app_name = "merchstore"