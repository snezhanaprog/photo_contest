from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from api.serializers.photo.serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticated
from api.services.photo.list import ListPhotoService
from api.services.photo.author_list import ListAuthorPhotoService
from api.services.photo.retrieve import RetrievePhotoService
from api.services.photo.delete import DeletePhotoService
from api.services.photo.update import UpdatePhotoService
from api.services.photo.create import CreatePhotoService
from utils.django_service_objects.service_objects.services import ServiceOutcome  # noqa: E501


class UploadPhotoView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        ServiceOutcome(
            CreatePhotoService,
            {**request.data.dict(), "author": request.user}
        )
        return Response(status=status.HTTP_200_OK)


class ListPublicPhotoView(APIView):
    def get(self, request):
        outcome = ServiceOutcome(ListPhotoService, request.GET.dict())
        return Response(
            PhotoSerializer(outcome.result, many=True).data,
            status=status.HTTP_200_OK
        )


class ListAuthorPhotoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            'status': request.GET.get('status'),
            "author": request.user.id
        }
        outcome = ServiceOutcome(ListAuthorPhotoService, data)
        return Response(
            PhotoSerializer(outcome.result, many=True).data,
            status=status.HTTP_200_OK
        )


class RetrievePhotoView(APIView):
    def get(self, request):
        outcome = ServiceOutcome(RetrievePhotoService, request.GET.dict())
        return Response(outcome, status=status.HTTP_200_OK)


class UpdatePhotoView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        outcome = ServiceOutcome(
            UpdatePhotoService,
            {**request.data.dict(), "author": request.user}
        )
        return Response(
            PhotoSerializer(outcome.data).data,
            status=status.HTTP_200_OK
        )


class DeletePhotoView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        outcome = ServiceOutcome(
            DeletePhotoService,
            {**request.data.dict(), "author": request.user}
        )
        return Response(outcome, status=status.HTTP_204_NO_CONTENT)
