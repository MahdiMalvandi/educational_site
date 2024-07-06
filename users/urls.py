from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *


urlpatterns = [
    path('register/', RegisterAndSendEmail.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', GetUserToken.as_view(), name='token_obtain_pair'),
    path('resend/', ResendCode.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('users/<username>/', UserProfileView.as_view(), name='user_profile'),
    # path('profile/', ProfileApiView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('change-password/', ChangePasswordApiView.as_view(), name='ChangePassword'),
    path('reset-password/', ForgotPasswordSendEmailApiView.as_view(), name='reset_password'),
    path('reset-password/confirm/', ForgotPasswordApiView.as_view(), name='reset_password_confirm'),
]
