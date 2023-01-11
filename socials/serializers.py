from rest_framework import serializers
from .models import Comment,Like
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Comment
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields=''
        model=Like