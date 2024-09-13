from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.registration.views import RegisterView
from .views.authorization.views import LoginView
from .views.photo.views import ListPublicPhotoView, ListAuthorPhotoView
from .views.photo.views import RetrievePhotoView, UploadPhotoView
from .views.user.views import UserProfileView
from .views.voice.views import StatusVoiceView
from .views.voice.views import ChangeStatusVoiceView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('photos/', ListPublicPhotoView.as_view(), name="photos"),
    path('users-photos/', ListAuthorPhotoView.as_view(),
         name='users-photo'),
    path('user-info/', UserProfileView.as_view(), name="user"),
    path('photos/<int:photo_id>/', RetrievePhotoView.as_view(), name="photo"),
    path('upload-photo/', UploadPhotoView.as_view(), name='upload-photo'),
    path('status-voice/', StatusVoiceView.as_view(), name="status-voice"),
    path('change-voice/', ChangeStatusVoiceView.as_view(), name="change-voice")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
