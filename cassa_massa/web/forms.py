from django.core.validators import MinLengthValidator
from django.forms import ModelForm, TextInput, EmailInput, NumberInput
from django import forms
from cassa_massa.web.models import Contact
from cassa_massa.web.validators import validate_only_letters


# class ContactForm(forms.Form):
#     class Meta:
#         model = Contact
#         fields = '__all__'
#
#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass

class ContactForm(forms.ModelForm):
    # NAME_MAX_LENGTH = 25
    # CELL_PHONE_MAX_LENGTH = 10
    # CELL_PHONE_MIN_LENGTH = 10
    # EMAIL_SUBJECT_MAX_LENGTH = 100
    # EMAIL_MESSAGE_MAX_LENGTH = 1000
    #
    # name = forms.CharField(
    #     max_length=NAME_MAX_LENGTH,
    #     validators=(
    #         validate_only_letters,
    #     )
    # )
    #
    # cell_phone_number = forms.CharField(
    #     max_length=CELL_PHONE_MAX_LENGTH,
    #     validators=(
    #         MinLengthValidator(CELL_PHONE_MIN_LENGTH),
    #     )
    # )
    #
    # email = forms.EmailField(
    #
    # )
    #
    # subject = forms.CharField(
    #     max_length=EMAIL_SUBJECT_MAX_LENGTH,
    # )
    #
    # message = forms.CharField(
    #     widget=forms.Textarea,
    #     max_length=EMAIL_MESSAGE_MAX_LENGTH,
    # )

    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'cell_phone_number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Telephone Number'
            }),
            'email': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'subject': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Subject'
            }),
            'message': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 700px; max-height: 100px',
                'placeholder': 'Message'
            }),
        }

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
