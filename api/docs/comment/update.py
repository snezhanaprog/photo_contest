from drf_yasg import openapi
from api.serializers.comment.serializers import CommentSerializer


MANUAL_PARAMS = [
    openapi.Parameter(
        name="content",
        in_=openapi.IN_BODY,
        description="Content",
        type=openapi.TYPE_STRING,
        required=True,
    ),
    openapi.Parameter(
        name="photo_id",
        in_=openapi.IN_BODY,
        description="Photo id",
        type=openapi.TYPE_INTEGER,
        required=True,
    ),
    openapi.Parameter(
        name="parent",
        in_=openapi.IN_BODY,
        description="Parent comment id",
        type=openapi.TYPE_INTEGER,
        required=False,
    ),
]

RESPONSES = {
    "201": openapi.Response(
        description="Success",
        schema=CommentSerializer(),
    ),
    "403": openapi.Response(
        description="Permission error",
        schema=openapi.Schema(
            title="PermissionError",
            type=openapi.TYPE_OBJECT,
            properties={
                "detail": openapi.Schema(type=openapi.TYPE_STRING,
                                         example="Permission error")
            },
        ),
    ),
    "400": openapi.Response(
        description="Invalid data",
        schema=openapi.Schema(
            title="ValidationError",
            type=openapi.TYPE_OBJECT,
            properties={
                "detail": openapi.Schema(type=openapi.TYPE_STRING,
                                         example="Invalid request data"),
            },
        ),
    ),
    "401": openapi.Response(
        description="Unauthorized",
    ),
    "404": openapi.Response(
        description="Comment or author not found",
        schema=openapi.Schema(
            title="NotFoundError",
            type=openapi.TYPE_OBJECT,
            properties={
                "comment_detail": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Comment does not exist"),
                "author_detail": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Author does not exist"),
            },
        ),
    ),
}

parameters = {
    "tags": ["Comment"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
