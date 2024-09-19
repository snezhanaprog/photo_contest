from drf_yasg import openapi


MANUAL_PARAMS = [
    openapi.Parameter(
        name='username',
        in_=openapi.IN_BODY,
        description='Username',
        type=openapi.TYPE_STRING,
        required=True,
    ),
    openapi.Parameter(
        name='password',
        in_=openapi.IN_BODY,
        description='Password',
        type=openapi.TYPE_STRING,
        required=True,
    ),
]

RESPONSES = {
    "200": openapi.Response(
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
    "401": openapi.Response(
        description="Unauthorized",
    ),
    "400": openapi.Response(
        description="Bad Request - Invalid input data",
    ),
}

parameters = {
    "tags": ["User"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
