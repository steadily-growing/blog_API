from rest_framework import serializers
from .models import Blog 

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields ='__all__'

