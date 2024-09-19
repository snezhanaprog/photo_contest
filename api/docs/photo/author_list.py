from drf_yasg import openapi
from api.serializers.photo.serializers import PhotoSerializer


def get_photo_properties():
    photo_fields = PhotoSerializer().get_fields()
    properties = {}

    for field_name, field in photo_fields.items():
        properties[field_name] = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description=field.help_text or "",
            example=field.default
        )
    return properties


MANUAL_PARAMS = [
    openapi.Parameter(
        name='status',
        in_=openapi.IN_QUERY,
        description='Sorting photos by status',
        type=openapi.TYPE_STRING,
        required=True,
    ),
]

RESPONSES = {
    "200": openapi.Response(
        description="Success",
        schema=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=get_photo_properties(),
            ),
        ),
    ),
    "401": openapi.Response(
        description="Unauthorized",
    ),
    "404": openapi.Response(
        description="Author not found",
        schema=openapi.Schema(
            title="NotFoundError",
            type=openapi.TYPE_OBJECT,
            properties={
                "detail": openapi.Schema(type=openapi.TYPE_STRING,
                                         example="Author does not exist"),
            },
        ),
    ),
}

parameters = {
    "tags": ["Photo"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
