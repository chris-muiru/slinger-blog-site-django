from rest_framework import serializers
from .models import Blog,Tag
from users.serializers import CustomUserSerializer
class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        fields='__all__'
        model=Tag

class BlogSerializer(serializers.ModelSerializer):
    tag=TagSerializer(many=True,read_only=True)
    writter=CustomUserSerializer(read_only=True)
    class Meta:
        model=Blog
        fields=['id','tag','blogTitle','blogContent','writter']