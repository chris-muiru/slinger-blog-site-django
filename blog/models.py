from django.db import models
from users.models import CustomUser
class Tag(models.Model):
    tagName=models.CharField(max_length=10)
    tagDescription=models.CharField(max_length=200,null=True)

class Blog(models.Model):
    blogTitle=models.CharField(max_length=100)
    blogContent=models.TextField()
    writter=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)

class BookMarkedBlog(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    blog_is_booked=models.BooleanField(default=True)

    
# Create your models here.
