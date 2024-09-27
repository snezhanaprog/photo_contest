from drf_yasg import openapi


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
    ),
}


parameters = {
    "tags": ["Photo"],
    "manual_parameters": MANUAL_PARAMS,
    "responses": RESPONSES,
}
