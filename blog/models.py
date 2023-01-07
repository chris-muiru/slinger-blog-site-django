from django.db import models
from users.models import CustomUser
class Tag(models.Model):
    tagName=models.CharField(max_length=10)
    tagDescription=models.CharField(max_length=200,null=True)
  
    def __str__(self):
        return self.tagName


class Blog(models.Model):
    blogTitle=models.CharField(max_length=100)
    blogContent=models.TextField()
    writter=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)
    def __str__(self):
        return self.blogTitle


class BookmarkedBlog(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    blog_is_booked=models.BooleanField(default=True)

    def __str__(self):
        return self.blog.blogTitle

class BlogPic(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE) 
    blogPic=models.ImageField(upload_to=blog)

    def __str__(self):
        return self.blog.blogTitle
# Create your models here.
