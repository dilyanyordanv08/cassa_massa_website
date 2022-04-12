from django.core.validators import MinLengthValidator
from django.forms import ModelForm
from django import forms
from cassa_massa.web.models import Contact

# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'
from cassa_massa.web.validators import validate_only_letters


class ContactForm(forms.Form):
    NAME_MAX_LENGTH = 25
    CELL_PHONE_MAX_LENGTH = 10
    CELL_PHONE_MIN_LENGTH = 10
    EMAIL_SUBJECT_MAX_LENGTH = 100
    EMAIL_MESSAGE_MAX_LENGTH = 1000

    name = forms.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    cell_phone_number = forms.CharField(
        max_length=CELL_PHONE_MAX_LENGTH,
        validators=(
            MinLengthValidator(CELL_PHONE_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    email = forms.EmailField(

    )

    subject = forms.CharField(
        max_length=EMAIL_SUBJECT_MAX_LENGTH,
    )

    message = forms.CharField(
        widget=forms.Textarea,
        max_length=EMAIL_MESSAGE_MAX_LENGTH,
    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
