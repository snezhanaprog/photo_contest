from django.urls import path
from .views.registration.views import RegisterView
from .views.authorization.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
