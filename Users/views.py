from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response

class RegisterUserAPIView(CreateAPIView):    
    permission_classes = (AllowAny,) 
    serializer_class = UserSerializer

    def post(self, request):
    	serializer = self.serializer_class(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
