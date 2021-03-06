from django.urls import path, include
from django.views.generic import TemplateView

from cassa_massa.auth_app.views import UserRegistrationView, UserLoginView, LogoutUserView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('change_password/', TemplateView.as_view(template_name='auth/change_password.html'), name='change password'),
    path('home_page/', TemplateView.as_view(template_name='home_page.html'), name='home page'),
)
