from django.urls import path
from cassa_massa.auth_app.views import UserRegistrationView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
)