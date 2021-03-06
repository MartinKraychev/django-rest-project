from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_project.api_auth.serializers import CreateUserSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class RegisterView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (
        AllowAny,
    )


class LoginView(ObtainAuthToken):
    permission_classes = (
        AllowAny,
    )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.id,
            'username': user.username
        })


class LogoutView(APIView):
    permission_classes = (
        IsAuthenticated,
    )

    @staticmethod
    def __perform_logout(request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({
            'message': 'User logged out'
        })

    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)
