from django.urls import path

from .views import (CustomPayloadController, PerfilUsuario)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('login-custom', CustomPayloadController.as_view()),
    path('refresh-token', TokenRefreshView.as_view()),
    path('verify-token', TokenVerifyView.as_view()),
    path('me', PerfilUsuario.as_view()),
]
