from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


UserModel = get_user_model()


# Extends UserRegistrationView with username, first name and last name
class UserRegistrationForm(UserCreationForm):
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
    success_url = reverse_lazy('index')

    # Stay logged after registering
    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


# TODO logout
class UserLogoutView(LogoutView):
    pass


