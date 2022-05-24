from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate

UserModel = get_user_model()


# Extends UserRegistrationView with username, first name and last name
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=15)

    class Meta:
        model = UserModel
        fields = ('email',)

    # TODO, later extend with validation for first name
    def clean_first_name(self):
        return self.cleaned_data['first_name']

    # TODO later extend with validation for last name
    def clean_last_name(self):
        return self.cleaned_data['last_name']


# Register form
class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('home page')

    # Stay logged after registering
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    next_page = 'home page'

    # def get_success_url(self):
    #     return reverse_lazy('home page')


# # TODO logout
# class UserLogoutView(LogoutView):
#     next_page = None


class LogoutUserView(LogoutView):
    next_page = None
    template_name = 'index_new.html'


class ChangePasswordView(PasswordResetView):
    pass
