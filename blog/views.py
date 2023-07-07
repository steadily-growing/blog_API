from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist




class BlogView(APIView): 
    #view all blogs
    def get(self, request):  
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)
    
    #create a blog
    def post(self,request):
        data = request.data
        serializer = BlogSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)



class BlogByIdView(APIView):
    def get_blog(self, id):
        try:
            return Blog.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({"error": "Not found."}, status=404)


    # View one blog by id
    def get(self, request, id=None):
        blog_instance = self.get_blog(id)
        if blog_instance:
            serializer = BlogSerializer(blog_instance)
            return Response(serializer.data, status=200)
        return Response({"error": "Not found."}, status=404)

    # Update blog
    def put(self, request, id=None):
        data = request.data
        blog_instance = self.get_blog(id)
        serializer = BlogSerializer(blog_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    # Delete blog
    def delete(self, request, id=None):
        blog_instance = self.get_blog(id)
        if blog_instance:
            blog_instance.delete()
            return Response(status=204)
        return Response({"error": "Not found."}, status=404)

            