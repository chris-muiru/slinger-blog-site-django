from django.urls import path
from .views import CommentView
urlpatterns=[
    path('comment/',CommentView.as_view(),name="comments")
    # path('like/')
]