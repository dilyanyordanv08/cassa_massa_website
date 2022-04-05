from django.urls import path, include
from cassa_massa.auth_app.views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view, name='logout user'),

    # path('accounts/', include('django.contrib.auth.urls')),
)