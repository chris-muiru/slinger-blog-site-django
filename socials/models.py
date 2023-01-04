from django.db import models
from blog.models import Blog
from users.models import CustomUser
class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.blog.blogName
# Create your models here.

class Like(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    blog_is_liked=models.BooleanField(default=True)
    def __str__(self):
        return self.blog.blogName
