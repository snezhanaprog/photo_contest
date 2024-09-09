from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.registration.views import RegisterView
from .views.authorization.views import LoginView
from .views.photo.views import PhotoListPublicView, PhotoListForAuthorView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('photos/', PhotoListPublicView.as_view(), name="photo"),
    path('users-photos/', PhotoListForAuthorView.as_view(), name='users-photo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
