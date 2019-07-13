from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Crear un nuevo usuario en el sistema"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """crea un nuevo token para los usuarios"""
    serializer_class = AuthTokenSerializer
    render_class = api_settings.DEFAULT_RENDERER_CLASSES
