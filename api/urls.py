from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.user.views import UserProfileView, RegisterView, LoginView
from .views.photo.views import ListPublicPhotoView, ListAuthorPhotoView
from .views.photo.views import RetrievePhotoView, UploadPhotoView
from .views.photo.views import UpdatePhotoView, DeletePhotoView
from .views.voice.views import CreateVoiceView, DeleteVoiceView
from .views.comment.views import ListCommentView, RetrieveCommentView
from .views.comment.views import CreateCommentView
from .views.comment.views import DeleteCommentView, UpdateCommentView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user-info/', UserProfileView.as_view(), name="user"),

    path('photos/', ListPublicPhotoView.as_view(), name="photos"),
    path('users-photos/', ListAuthorPhotoView.as_view(),
         name='users-photo'),
    path('photo/<int:id>/', RetrievePhotoView.as_view(), name="photo"),
    path('upload-photo/', UploadPhotoView.as_view(), name='upload-photo'),
    path('delete-photo/<int:id>/', DeletePhotoView.as_view(),
         name="delete-photo"),
    path('update-photo/<int:id>', UpdatePhotoView.as_view(),
         name='update-photo'),

    path('delete-voice/', DeleteVoiceView.as_view(), name="delete-voice"),
    path('create-voice/', CreateVoiceView.as_view(), name="create-voice"),

    path('comments/', ListCommentView.as_view(), name="comments"),
    path('comment/<int:id>/', RetrieveCommentView.as_view(), name="comment"),
    path('create-comment/', CreateCommentView.as_view(),
         name='create-comment'),
    path('delete-comment/<int:id>/', DeleteCommentView.as_view(),
         name="delete-comment"),
    path('update-comment/<int:id>', UpdateCommentView.as_view(),
         name='update-comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
