from django.shortcuts import render

from auth.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    # for simplejwt authentication
    serializer_class = MyTokenObtainPairSerializer