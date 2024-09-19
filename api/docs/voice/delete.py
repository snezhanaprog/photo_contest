from drf_yasg import openapi


MANUAL_PARAMS = [
    openapi.Parameter(
        name='photo_id',
        in_=openapi.IN_BODY,
        description='Photo id',
        type=openapi.TYPE_INTEGER,
        required=True,
    ),
]

RESPONSES = {
    "204": openapi.Response(
        description="Success"
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
    "tags": ["Voice"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
