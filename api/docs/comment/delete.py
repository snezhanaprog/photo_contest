from drf_yasg import openapi


MANUAL_PARAMS = [
    openapi.Parameter(
        name="id",
        in_=openapi.IN_PATH,
        description="Comment id",
        type=openapi.TYPE_INTEGER,
        required=True,
    )
]

RESPONSES = {
    "204": openapi.Response(
        description="Success"
    ),
    "403": openapi.Response(
        description="Permission error",
        schema=openapi.Schema(
            title="PermissionError",
            type=openapi.TYPE_OBJECT,
            properties={
                "detail": openapi.Schema(type=openapi.TYPE_STRING,
                                         example="Permission error")
            },
        ),
    ),
    "401": openapi.Response(
        description="Unauthorized",
    ),
    "404": openapi.Response(
        description="Comment or author not found",
        schema=openapi.Schema(
            title="ValidationError",
            type=openapi.TYPE_OBJECT,
            properties={
                "comment_detail": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Comment does not exist"),
                "author_detail": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Author does not exist")
            },
        ),
    ),
}

parameters = {
    "tags": ["Comment"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
