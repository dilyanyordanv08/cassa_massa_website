from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
