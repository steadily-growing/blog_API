from django.urls import path
from .views import BlogAPIView

urlpatterns = [
    path('blogs/', BlogAPIView.as_view(), name='blog-list'),  # For GET request
    path('blogs/', BlogAPIView.as_view(), name='blog-create'),  # For POST request
]
