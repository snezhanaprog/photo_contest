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
from api.docs.photo.create import parameters as create_parameters
from api.docs.photo.delete import parameters as delete_parameters
from api.docs.photo.list import parameters as list_parameters
from api.docs.photo.author_list import parameters as author_list_parameters
from api.docs.photo.retrieve import parameters as retrieve_parameters
from api.docs.photo.update import parameters as update_parameters
from drf_yasg.utils import swagger_auto_schema


class UploadPhotoView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(**create_parameters)
    def post(self, request):
        outcome = ServiceOutcome(
            CreatePhotoService,
            {**request.data.dict(), "author_id": request.user.id}
        )
        return Response(
            PhotoSerializer(outcome.result).data,
            status=status.HTTP_201_CREATED
        )


class ListPublicPhotoView(APIView):
    @swagger_auto_schema(**list_parameters)
    def get(self, request):
        outcome = ServiceOutcome(ListPhotoService, request.GET.dict())
        return Response({
            "pagination": outcome.result['pagination'].to_json(),
            "photos": PhotoSerializer(
                outcome.result['photos'],
                context={'user': request.user},
                many=True).data
            }, status=status.HTTP_200_OK)


class ListAuthorPhotoView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**author_list_parameters)
    def get(self, request):
        data = {
            **request.GET.dict(),
            "author_id": request.user.id
        }
        outcome = ServiceOutcome(ListAuthorPhotoService, data)
        return Response({
            "pagination": outcome.result['pagination'].to_json(),
            "photos": PhotoSerializer(
                outcome.result['photos'], many=True).data
            }, status=status.HTTP_200_OK)


class RetrievePhotoView(APIView):
    @swagger_auto_schema(**retrieve_parameters)
    def get(self, request, id):
        outcome = ServiceOutcome(RetrievePhotoService,
                                 {'id': id, "author_id": request.user.id})
        return Response(
            PhotoSerializer(
                outcome.result,
                context={'user': request.user}).data,
            status=status.HTTP_200_OK)


class UpdatePhotoView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**update_parameters)
    def put(self, request, id):
        outcome = ServiceOutcome(
            UpdatePhotoService,
            {**request.data.dict(), "author_id": request.user.id, "id": id}
        )
        return Response(
            PhotoSerializer(outcome.result).data,
            status=status.HTTP_200_OK
        )


class DeletePhotoView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**delete_parameters)
    def delete(self, request, id):
        ServiceOutcome(
            DeletePhotoService,
            {"author_id": request.user.id, "id": id}
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
