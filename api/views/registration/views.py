from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from api.services.user.create import CreateUserService


class RegisterView(APIView):
    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        try:
            service = CreateUserService({
                'username': username,
                'email': email,
                'password': password,
            })
            user = service.process()
            print("1")
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
