from django.urls import path, include
from cassa_massa.auth_app.views import UserRegistrationView, UserLoginView, UserLogoutView
from cassa_massa.web import views

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    # path('logout/', views.logout, name='logout'),

    # path('accounts/', include('django.contrib.auth.urls')),
)
