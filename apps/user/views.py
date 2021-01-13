from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistrationAPISerializer

User = get_user_model()


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationAPISerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
#email
#password1
#password2


