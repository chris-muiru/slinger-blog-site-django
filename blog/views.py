from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog,Tag
from rest_framework.decorators import api_view
from .serializers import BlogSerializer,TagSerializer
from django.http import Http404
class BlogView(APIView):
    def get(self,request):
        query=Blog.objects.all()
        serialize=BlogSerializer(query,many=True)
        return Response(serialize.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writter=request.user)
            return Response(serializer.validated_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TagView(APIView):
    def get(self,request):
        querySet=Tag.objects.all()
        serializer=TagSerializer(querySet,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class TagDetailView(APIView):
    def get_object(self,pk):
        try:
            return Tag.objects.get(id=pk)
        except Tag.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        query=self.get_object(pk)
        serializer=TagSerializer(query)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        query=self.get_object(pk)
        serializer=TagSerializer(query,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        query=self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)