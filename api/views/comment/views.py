from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.comment.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from api.services.comment.list import ListCommentService
from api.services.comment.retrieve import RetrieveCommentService
from api.services.comment.delete import DeleteCommentService
from api.services.comment.update import UpdateCommentService
from api.services.comment.create import CreateCommentService
from utils.django_service_objects.service_objects.services import ServiceOutcome  # noqa: E501


class CreateCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        outcome = ServiceOutcome(
            CreateCommentService,
            {**request.data.dict(), "author_id": request.user.id}
        )
        return Response(
            CommentSerializer(outcome.result).data,
            status=status.HTTP_200_OK
        )


class ListCommentView(APIView):
    def get(self, request):
        outcome = ServiceOutcome(ListCommentService, request.GET.dict())
        return Response(
            CommentSerializer(outcome.result, many=True).data,
            status=status.HTTP_200_OK
        )


class RetrieveCommentView(APIView):
    def get(self, request, id):
        outcome = ServiceOutcome(RetrieveCommentService,
                                 {'id': id, "author_id": request.user.id})
        return Response(
            CommentSerializer(outcome.result).data,
            status=status.HTTP_200_OK
        )


class UpdateCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        outcome = ServiceOutcome(
            UpdateCommentService,
            {**request.data.dict(), "author_id": request.user.id, 'id': id}
        )
        return Response(
            CommentSerializer(outcome.result).data,
            status=status.HTTP_200_OK
        )


class DeleteCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        ServiceOutcome(
            DeleteCommentService,
            {"author_id": request.user.id, 'id': id}
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
