from rest_framework import serializers
from .models import Blog,Tag,BookmarkedBlog
from users.serializers import CustomUserSerializer
class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        fields='__all__'
        model=Tag
        
class BlogSerializer(serializers.ModelSerializer):
    tag= TagSerializer(many=True)
    writter=serializers.ReadOnlyField(source='writter.username')
    class Meta:
        model=Blog
        fields=['id','tag','blogTitle','blogContent','writter']
        
  
    def create(self,validated_data):
        print(validated_data)
        tags=validated_data.pop('tag')
        arrTags=[]
        for tag in tags:
            obj,created=Tag.objects.get_or_create(tagName=tag['tagName'])
            arrTags.append(obj)
        
        blog=Blog.objects.create(**validated_data)
        blog.tag.add(*arrTags)
        return Blog.objects.filter(blogTitle=validated_data['blogTitle'])

class BookmarkedBlogSerializer(serializers.ModelSerializer):
    blog=BlogSerializer(read_only=True)
    blog_id=serializers.PrimaryKeyRelatedField(
        queryset=Blog.objects.all(),
        write_only=True,
        source='blog'  #TODO why does it return {blog:instance} instead of {blog_id: instance} in validated_data
    )
    class Meta:
        fields=['blog','blog_id']
        model=BookmarkedBlog
    def create(self,validated_data):
        print(validated_data)
        obj,created = BookmarkedBlog.objects.get_or_create(blog=validated_data['blog'])  
        return obj


    # another implementation is by using SerializerMethodField() 
    # blog=serializers.SerializerMethodField() 
    # def get_blog(self, obj):
    #     return BlogSerializer(obj.blog).data