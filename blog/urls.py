from django.urls import path 
from .views import BlogView,TagView,BookmarkedBlogView
urlpatterns = [
    path('',BlogView.as_view()),
    path('book/',BookmarkedBlogView.as_view()),
    path('tag/',TagView.as_view())
]
