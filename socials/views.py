from django.shortcuts import render
from rest_framework.views import APIView

from blog.models import Blog
from .models import Comment,Like
from .serializers import CommentSerializer,LikeSerializer 
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404


class CommentView(APIView):
    def get(self,request):
        query=Comment.objects.all()
        serializer=CommentSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    def post(self,request):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def get_object(self,pk):
        try:
            return Comment.objects.get(id=pk)
        except Comment.DoesNotExist:
            return Http404
            
    def get(self,request,pk):
        query=self.get_object(pk) 
        serializer=CommentSerializer(query)
        return Response(serializer,status=status.HTTP_200_OK)

    def put(self,request,pk):
        query=self.get_object(pk)
        serializer=CommentSerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        query=self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeView(APIView):
    # TODO: hmmmmmmmmmmmm.....toggle functionality in post??
    def get(self,request,pk):
        query=Like.objects.filter(blog=pk).count()
        return Response(query,status=status.HTTP_200_OK) 
    def post(self,request,pk):
        blogInstance= get_object_or_404(Blog,id=pk)
        query=Like.objects.filter(blog=blogInstance,sender=request.user)
        if query:
            query.delete()
            return Response({"detail":"unliked"},status=status.HTTP_200_OK)
        createInstance=Like.objects.create(blog=blogInstance,sender=request.user)
        return Response({"detail":"liked"},status=status.HTTP_200_OK)

        
            
         