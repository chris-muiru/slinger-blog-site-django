from django.urls import path
from .views import SignUpCustomUserView
urlpatterns = [
    path('sign-up/',SignUpCustomUserView.as_view()),
]
