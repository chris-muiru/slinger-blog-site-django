from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
class SignUpCustomUserView(APIView):
    def post(self,request):
        serializer=CustomUserSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response({},status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomUserView(APIView):
    pass
 
class CustomUserDetailView(APIView):
    def get(self,request,pk):
        pass
    def put(self,request,pk):
        pass
    def delete(self,request,pk):
        pass