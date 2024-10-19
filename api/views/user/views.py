from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from api.serializers.user.serializers import UserSerializer, ProfileSerializer
from api.serializers.user.serializers import GoogleSocialAuthSerializer
from api.services.user.retrieve import RetrieveUserService
from rest_framework.permissions import IsAuthenticated
from utils.django_service_objects.service_objects.services import ServiceOutcome  # noqa: E501
from rest_framework import status
from api.services.token.retrieve import RetrieveTokenService
from api.services.user.create import CreateUserService
from api.services.avatar.upload import UploadAvatarService
from api.docs.user.authorization import parameters as authorization_parameters
from api.docs.user.registration import parameters as registration_parameters
from api.docs.user.retrieve import parameters as retrieve_parameters
from drf_yasg.utils import swagger_auto_schema
from api.docs.user.avatar import parameters as avatar_parameters
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes as permission


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(**retrieve_parameters)
    def get(self, request):
        outcome = ServiceOutcome(RetrieveUserService, {'id': request.user.id})
        return Response({
                   'user': UserSerializer(outcome.result['user']).data,
                   'profile': ProfileSerializer(outcome.result['profile']).data
                }, status=status.HTTP_200_OK)


class UploadAvatarView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(**avatar_parameters)
    def post(self, request):
        ServiceOutcome(
            UploadAvatarService,
            {**request.data.dict(), "user_id": request.user.id}
        )
        return Response(status=status.HTTP_201_CREATED)


class RegisterView(APIView):
    @swagger_auto_schema(**registration_parameters)
    def post(self, request):
        ServiceOutcome(CreateUserService, request.data)
        outcome = ServiceOutcome(RetrieveTokenService, request.data)
        return Response(
            {'auth_token': str(outcome.result)},
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    @swagger_auto_schema(**authorization_parameters)
    def post(self, request):
        outcome = ServiceOutcome(RetrieveTokenService, request.data)
        return Response(
            {'auth_token': str(outcome.result)},
            status=status.HTTP_200_OK
        )


@permission((AllowAny, ))
class GoogleSocialAuthView(APIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)
