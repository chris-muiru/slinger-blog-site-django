from django.shortcuts import render
from rest_framework.views import APIView
from .models import Comment,Like
from .serializers import CommentSerializer,LikeSerializer 
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class CommentView(APIView):
    def get(self,request):
        query=Comment.objects.all()
        serializer=CommentSerializer(query)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    def post(self,request):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class LikeView(APIView):
    def get(self,request):
        query=Like.objects.all()
        serializer=LikeSerializer(query)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    def post(self,request):
        serializer=LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 