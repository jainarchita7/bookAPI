from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import UserRateThrottle
from .models import Book
from .serializers import BookSerializer

# Define a rate-limiting throttle
class BookThrottle(UserRateThrottle):
    rate = '5/min'

class BookView(APIView):
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]          
    throttle_classes = [BookThrottle]            

    def post(self, request):
        serializer = BookSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)