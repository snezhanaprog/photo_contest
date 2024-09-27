from drf_yasg import openapi
from api.serializers.user.serializers import UserSerializer
from api.serializers.user.serializers import ProfileSerializer


MANUAL_PARAMS = []


RESPONSES = {
    "200": openapi.Response(
        description="Success",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': UserSerializer().data,
                'profile': ProfileSerializer().data,
            },
        ),
    ),
    "401": openapi.Response(
        description="Unauthorized",
    ),
    "404": openapi.Response(
        description="User not found",
        schema=openapi.Schema(
            title="ValidationError",
            type=openapi.TYPE_OBJECT,
            properties={
                "type": openapi.Schema(type=openapi.TYPE_STRING,
                                       example="ServiceObjectLogicError"),
                "message": openapi.Schema(type=openapi.TYPE_STRING,
                                          example="User does not exist"),
                "translation_key": openapi.Schema(type=openapi.TYPE_STRING,
                                                  example="user_not_found"),
            },
        ),
    ),
}

parameters = {
    "tags": ["User"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
