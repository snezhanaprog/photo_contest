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
        name='search',
        in_=openapi.IN_QUERY,
        description='Search query for filtering photos',
        type=openapi.TYPE_STRING,
        required=False,
    ),
    openapi.Parameter(
        name='sort',
        in_=openapi.IN_QUERY,
        description='Sorting photos',
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
}

REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties=get_photo_properties(),
)


parameters = {
    "tags": ["Photo"],
    "manual_parameters": MANUAL_PARAMS,
    "request_body": REQUEST_BODY,
    "responses": RESPONSES,
}
