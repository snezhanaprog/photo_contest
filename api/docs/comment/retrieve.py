from drf_yasg import openapi
from api.serializers.comment.serializers import CommentSerializer


MANUAL_PARAMS = [
    openapi.Parameter(
        name="id",
        in_=openapi.IN_PATH,
        description="Comment id",
        type=openapi.TYPE_INTEGER,
        required=True,
    )
]


RESPONSES = {
    "200": openapi.Response(
        description="Success",
        schema=CommentSerializer(),
    ),
    "404": openapi.Response(
        description="Comment not found",
        schema=openapi.Schema(
            title="ValidationError",
            type=openapi.TYPE_OBJECT,
            properties={
                "type": openapi.Schema(type=openapi.TYPE_STRING,
                                       example="ServiceObjectLogicError"),
                "message": openapi.Schema(type=openapi.TYPE_STRING,
                                          example="Comment does not exist"),
                "translation_key": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="comment_not_found"),
            },
        ),
    ),
}

parameters = {
    "tags": ["Comment"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
