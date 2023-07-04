from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer


class BlogView(APIView): 
    def get(self, request):  
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)
    
    def post(self,request):
        data = request.data
        serializer = BlogSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
