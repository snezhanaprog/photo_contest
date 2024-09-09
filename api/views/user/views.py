from rest_framework.views import APIView
from rest_framework.response import Response
from api.services.user.element import ElementUserService
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        service = ElementUserService(data={'username': request.user.username})

        if service.is_valid():
            user_profile = service.process()
            if user_profile['profile'].avatar:
                avatar_url = user_profile['profile'].avatar.url
            else:
                avatar_url = None
            return Response({
                'user': {
                    'username': user_profile['user'].username,
                    'email': user_profile['user'].email,
                },
                'profile': {
                    'avatar': avatar_url,
                }
            })
        else:
            return Response({'error': service.errors}, status=400)
