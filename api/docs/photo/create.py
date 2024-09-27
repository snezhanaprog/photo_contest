from drf_yasg import openapi
from api.serializers.photo.serializers import PhotoSerializer


MANUAL_PARAMS = [
    openapi.Parameter(
        name="title",
        in_=openapi.IN_FORM,
        description="Photo title",
        type=openapi.TYPE_STRING,
        required=True,
    ),
    openapi.Parameter(
        name="description",
        in_=openapi.IN_FORM,
        description="Photo description",
        type=openapi.TYPE_STRING,
        required=True,
    ),
    openapi.Parameter(
        name="image",
        in_=openapi.IN_FORM,
        description="Photo image data",
        type=openapi.TYPE_FILE,
        required=True,
    ),
]

RESPONSES = {
    "201": openapi.Response(
        description="Success",
        schema=PhotoSerializer(),
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
        description="Author not found",
        schema=openapi.Schema(
            title="NotFoundError",
            type=openapi.TYPE_OBJECT,
            properties={
                "detail": openapi.Schema(type=openapi.TYPE_STRING,
                                         example="Author does not exist"),
            },
        ),
    )
}

parameters = {
    "tags": ["Photo"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
