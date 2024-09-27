from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from api.serializers.comment.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from api.services.comment.list import ListCommentService
from api.services.comment.retrieve import RetrieveCommentService
from api.services.comment.delete import DeleteCommentService
from api.services.comment.update import UpdateCommentService
from api.services.comment.create import CreateCommentService
from utils.django_service_objects.service_objects.services import ServiceOutcome  # noqa: E501
from drf_yasg.utils import swagger_auto_schema
from api.docs.comment.create import parameters as create_parameters
from api.docs.comment.delete import parameters as delete_parameters
from api.docs.comment.list import parameters as list_parameters
from api.docs.comment.retrieve import parameters as retrieve_parameters
from api.docs.comment.update import parameters as update_parameters


class CreateCommentView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (FormParser,)

    @swagger_auto_schema(**create_parameters)
    def post(self, request):
        outcome = ServiceOutcome(
            CreateCommentService,
            {**request.data.dict(), "author_id": request.user.id}
        )
        return Response(
            CommentSerializer(outcome.result).data,
            status=status.HTTP_201_CREATED
        )


class ListCommentView(APIView):
    @swagger_auto_schema(**list_parameters)
    def get(self, request):
        outcome = ServiceOutcome(ListCommentService, request.GET.dict())
        return Response(
            CommentSerializer(
                outcome.result,
                context={'user': request.user},
                many=True).data,
            status=status.HTTP_200_OK
        )


class RetrieveCommentView(APIView):
    @swagger_auto_schema(**retrieve_parameters)
    def get(self, request, id):
        outcome = ServiceOutcome(RetrieveCommentService,
                                 {'id': id, "author_id": request.user.id})
        return Response(
            CommentSerializer(
                outcome.result,
                context={'user': request.user}).data,
            status=status.HTTP_200_OK
        )


class UpdateCommentView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (FormParser,)

    @swagger_auto_schema(**update_parameters)
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

    @swagger_auto_schema(**delete_parameters)
    def delete(self, request, id):
        ServiceOutcome(
            DeleteCommentService,
            {"author_id": request.user.id, 'id': id}
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
