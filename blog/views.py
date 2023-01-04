from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from rest_framework.decorators import api_view
from .serializers import BlogSerializer
class BlogView(APIView):
    def get(self,request):
        query=Blog.objects.all()
        serialized=BlogSerializer(query,many=True)
        print(serialized.data)
        return Response(serialized.data,status=status.HTTP_200_OK)
# Create your views here.
