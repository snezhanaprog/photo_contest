from drf_yasg import openapi


MANUAL_PARAMS = [
    openapi.Parameter(
        name="avatar",
        in_=openapi.IN_BODY,
        description="Avatar image data",
        type=openapi.TYPE_FILE,
        required=True,
    ),
]

RESPONSES = {
    "201": openapi.Response(
        description="Success",
    ),
    "401": openapi.Response(
        description="Unauthorized",
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
    "404": openapi.Response(
        description="User or profile not found",
        schema=openapi.Schema(
            title="NotFoundError",
            type=openapi.TYPE_OBJECT,
            properties={
                "user_detail": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="User does not exist"),
                "profile_detail": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Profile does not exist"),
            },
        ),
    ),
}

parameters = {
    "tags": ["Profile"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
