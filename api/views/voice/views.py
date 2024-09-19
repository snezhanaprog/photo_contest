from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.voice.serializers import VoiceSerializer
from rest_framework.permissions import IsAuthenticated
from api.services.voice.delete import DeleteVoiceService
from api.services.voice.create import CreateVoiceService
from utils.django_service_objects.service_objects.services import ServiceOutcome  # noqa: E501
from api.docs.voice.create import parameters as create_parameters
from api.docs.voice.delete import parameters as delete_parameters
from drf_yasg.utils import swagger_auto_schema


class CreateVoiceView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**create_parameters)
    def post(self, request):
        outcome = ServiceOutcome(
            CreateVoiceService,
            {**request.data, "author_id": request.user.id}
        )
        return Response(
            VoiceSerializer(outcome.result).data,
            status=status.HTTP_200_OK
            )


class DeleteVoiceView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**delete_parameters)
    def post(self, request):
        ServiceOutcome(
            DeleteVoiceService,
            {**request.data, "author_id": request.user.id}
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
