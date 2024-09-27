from drf_yasg import openapi
from api.serializers.comment.serializers import CommentSerializer


def get_comment_properties():
    comment_fields = CommentSerializer().get_fields()
    properties = {}

    for field_name, field in comment_fields.items():
        properties[field_name] = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description=field.help_text or "",
            example=field.default
        )
    return properties


MANUAL_PARAMS = [
    openapi.Parameter(
        name="photo_id",
        in_=openapi.IN_QUERY,
        description="Photo id",
        type=openapi.TYPE_INTEGER,
        required=True,
    ),
    openapi.Parameter(
        name="parent",
        in_=openapi.IN_QUERY,
        description="Parent comment id",
        type=openapi.TYPE_INTEGER,
        required=False,
    )
]

RESPONSES = {
    "200": openapi.Response(
        description="Success",
        schema=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=None,
            ),
        ),
    ),
    "404": openapi.Response(
        description="Photo not found",
        schema=openapi.Schema(
            title="NotFoundError",
            type=openapi.TYPE_OBJECT,
            properties={
                "detail": openapi.Schema(type=openapi.TYPE_STRING,
                                         example="Photo does not exist"),
            },
        ),
    ),
}

parameters = {
    "tags": ["Comment"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
