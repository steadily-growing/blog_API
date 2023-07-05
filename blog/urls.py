from django.urls import path
from .views import BlogView, BlogByIdView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blog-list'),  # For GET request
    path('blogs/add/', BlogView.as_view(), name='blog-create'), # For POST request
    path('blogs/<int:id>/', BlogByIdView.as_view(), name='view-blog-by-id'),
]
