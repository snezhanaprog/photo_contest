from drf_yasg import openapi
from api.serializers.comment.serializers import CommentSerializer


MANUAL_PARAMS = [
    openapi.Parameter(
        name="content",
        in_=openapi.IN_FORM,
        description="Content",
        type=openapi.TYPE_STRING,
        required=True,
    ),
    openapi.Parameter(
        name="photo_id",
        in_=openapi.IN_FORM,
        description="Photo id",
        type=openapi.TYPE_INTEGER,
        required=True,
    ),
    openapi.Parameter(
        name="parent",
        in_=openapi.IN_FORM,
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
        description="Photo comment or author not found",
        schema=openapi.Schema(
            title="NotFoundError",
            type=openapi.TYPE_OBJECT,
            properties={
                "photo_detail": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Photo does not exist"),
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
