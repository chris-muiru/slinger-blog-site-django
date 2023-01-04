from rest_framework import serializers
from .models import Blog,Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        fields='__all__'
        model=Tag
class BlogSerializer(serializers.ModelSerializer):
    tag=TagSerializer(many=True,read_only=True)
    class Meta:
        model=Blog
        fields=['id','tag','blogTitle','blogContent','writter']