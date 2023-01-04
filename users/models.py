from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    customUserEmail=models.EmailField(unique=True)
    username=models.CharField(unique=True,max_length=50)
    customUserPhone=models.IntegerField(null=True) 
    USERNAME_FIELD="customUserEmail"
    REQUIRED_FIELDS=["username"]

class CustomUserProfile(models.Model):
    customUser=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    customUserProfilePicture=models.ImageField(upload_to='CustomUserProfile')
 
# class Follower(models.Model):
#     user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     follower=models.ManyToManyField(CustomUser)
