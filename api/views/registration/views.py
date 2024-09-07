from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from api.services.user import create


class RegisterView(APIView):
    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password or not email:
            return Response(
                {'error': 'Все поля обязательны для заполнения'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'Пользователь с таким именем уже существует'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = create.CreateUserService.execute({
                'username': username,
                'email': email,
                'password': password,
            })
            token = Token.objects.create(user=user)
            return Response(
                {'auth_token': str(token)},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {'status': 'error', 'errors': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
