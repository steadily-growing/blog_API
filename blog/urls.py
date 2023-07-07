from django.urls import path
from .views import BlogView, BlogByIdView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='list'), 
    path('blogs/<int:id>/', BlogByIdView.as_view(), name='by-id'),
]
