from django.db import models
from blog.models import Blog
from users.models import CustomUser
from django.utils import timezone
class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    createdAt=models.DateTimeField(auto_now_add=timezone.now)
    def __str__(self):
        return self.blog.blogTitle
# Create your models here.
# 
class Like(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_liked=models.BooleanField(default=True)
    def __str__(self):
        return self.blog.blogTitle
