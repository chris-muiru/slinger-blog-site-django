from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
class CustomUserView(APIView):
    def get(self,request):
        queryset=CustomUser.objects.all()
        serializer=CustomUserSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
# Create your views here.
