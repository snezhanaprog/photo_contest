from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.comment.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from api.services.comment.list import ListCommentService
from api.services.comment.element import ItemCommentService
from api.services.comment.delete import DeleteCommentService
from api.services.comment.update import UpdateCommentService
from api.services.comment.create import CreateCommentService


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        service = CreateCommentService(data=request.data)
        comment = service.process(author=self.request.user)
        try:
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            ValueError("Ошибка создания комментария:", e)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ListCommentService()

    def get_queryset(self):
        parent = self.request.GET.get('parent', None)
        comments = self.service.process(parent=parent)
        if comments is None:
            comments = []
        return comments

    def get(self, request):
        try:
            comments = self.get_queryset()
            comments = list(comments)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class CommentItemView(APIView):
    def get(self, request, comment_id):
        service = ItemCommentService(data={'comment_id': comment_id})
        if service.is_valid():
            comment = service.process()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, comment_id):
        service = UpdateCommentService(data={**request.data,
                                             'comment_id': comment_id})
        if service.is_valid():
            comment = service.process(author=request.user)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, comment_id):
        service = DeleteCommentService(data={'comment_id': comment_id})
        if service.is_valid():
            service.process(author=request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)
