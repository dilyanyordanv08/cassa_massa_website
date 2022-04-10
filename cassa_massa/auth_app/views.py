from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.contrib.messages.context_processors import messages
from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from cassa_massa.auth_app.models import Profile
from django.contrib.auth import logout as auth_logout


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

    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     profile = Profile(
    #         **self.cleaned_data,
    #         user=user,
    #     )
    #     if commit:
    #         profile.save()
    #
    #     return user


# Register form
class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')

    # Stay logged after registering
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


# TODO logout
class UserLogoutView(LogoutView):
    next_page = None

# def logout_user(request):
#     logout(request)
#     messages.success(request, "you are logged out")
#     return redirect('home')

