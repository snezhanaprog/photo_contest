from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.photo.serializers import PhotoSerializer
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


class PhotoListPublicView(APIView):
    async def get_queryset(self):
        service = ListPhotoService()
        search = self.request.GET.get('search')
        sort = self.request.GET.get('sort')
        return await service.process(search=search, sort=sort, status="public")

    async def get(self, request):
        try:
            photos = await self.get_queryset()
            serializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class PhotoListForAuthorView(APIView):
    permission_classes = [IsAuthenticated]

    async def get_queryset(self):
        service = ListPhotoService()
        search = self.request.GET.get('search')
        sort = self.request.GET.get('sort')
        status = self.request.GET.get('status', 'public')

        return await service.process_for_author(
                search=search,
                sort=sort,
                status=status,
                author=self.request.user
            )

    async def get(self, request):
        try:
            photos = await self.get_queryset()
            serializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class PhotoItemView(APIView):
    def get(self, request, photo_id):
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
            photo = service.process(author=request.user)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, photo_id):
        service = DeletePhotoService(data={'photo_id': photo_id})
        if service.is_valid():
            service.process(author=request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)
