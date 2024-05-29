from django.urls import path
from .views import api_home, SearchApiView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('', api_home),
    path('auth/', obtain_auth_token),
    path('search/', SearchApiView.as_view(), name='search-view'),
    path('token/', TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]