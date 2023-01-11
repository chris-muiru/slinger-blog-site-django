from django.urls import path
from .views import CommentView,LikeView
urlpatterns=[
    path('comment/',CommentView.as_view(),name="comments"),
    path('like/<int:pk>/',LikeView.as_view())
]