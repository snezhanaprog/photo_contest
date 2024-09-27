from drf_yasg import openapi


REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['photo_id'],
    properties={
        'photo_id': openapi.Schema(type=openapi.TYPE_INTEGER)
    }
)

RESPONSES = {
    "200": openapi.Response(
        description="Success",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'voice': openapi.Schema(type=openapi.TYPE_OBJECT,
                                        description='Voice created'),
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
    "request_body": REQUEST_BODY,
    "responses": RESPONSES,
}
