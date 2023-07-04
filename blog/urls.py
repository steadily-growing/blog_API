from django.urls import path
from .views import BlogView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blog-list'),  # For GET request
    path('blogs/add', BlogView.as_view(), name='blog-create'),  # For POST request
]
