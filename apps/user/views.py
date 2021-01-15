from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistrationAPISerializers, LoginSerializer
from .utils import send_activation_mail

User = get_user_model()


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationAPISerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                user.create_activation_code()
                send_activation_mail(user.email, user.activation_code)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivationView(APIView):

    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.activate_with_code(activation_code)
        return Response(data={'message': 'Аккаунт успешно активирован'}, status=status.HTTP_200_OK)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно вышли с аккаунта.', status=status.HTTP_200_OK)




#email
#password1
#password2


