from django.urls import path 
from .views import BlogView,TagView
urlpatterns = [
    path('',BlogView.as_view()),
    path('tag/',TagView.as_view())
]
