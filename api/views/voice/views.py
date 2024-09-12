from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.services.voice.delete import DeleteVoiceService
from api.services.voice.create import CreateVoiceService
from api.services.voice.status import StatusVoiceService


class ChangeStatusVoiceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.data['status']:
            service = DeleteVoiceService(data=request.data)
            status_voice = False
        else:
            service = CreateVoiceService(data=request.data)
            status_voice = True
        try:
            voice = service.process(author=self.request.user)
            print(voice)
            return Response(
                {'status': str(status_voice)}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print("Ошибка обработки голоса:", e)
            ValueError("Ошибка обработки голоса:", e)
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)


class StatusVoiceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        service = StatusVoiceService(data=request.data)
        status_voice = service.process(author=self.request.user)
        return Response(
            {'success': status_voice}, status=status.HTTP_201_CREATED
        )
