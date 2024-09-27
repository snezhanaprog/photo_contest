from drf_yasg import openapi

REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['username', 'password', 'email'],
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
    }
)

RESPONSES = {
    "201": openapi.Response(
        description="Success",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'auth_token': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Authentication token'),
            },
        ),
    ),
    "400": openapi.Response(
        description="Bad Request - Invalid input data",
    ),
}

parameters = {
    "tags": ["User"],
    "request_body": REQUEST_BODY,
    "responses": RESPONSES,
}
