from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.photo import PhotoSerializer
from rest_framework.permissions import IsAuthenticated
from api.services.photo.list import ListPhotoService
from api.services.photo.element import ItemPhotoService
from api.services.photo.delete import DeletePhotoService
from api.services.photo.update import UpdatePhotoService


class PhotoUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoListView(APIView):
    def get(self, request):
        service = ListPhotoService()
        photos = service.process()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PhotoItemView(APIView):
    def get(self, reques, photo_id):
        service = ItemPhotoService(data={'photo_id': photo_id})
        if service.is_valid():
            photo = service.process()
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, photo_id):
        service = UpdatePhotoService(data={**request.data,
                                           'photo_id': photo_id})
        if service.is_valid():
            photo = service.process()
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, photo_id):
        service = DeletePhotoService(data={'photo_id': photo_id})
        if service.is_valid():
            service.process()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)
