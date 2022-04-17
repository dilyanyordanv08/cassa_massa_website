from django.core.validators import MinLengthValidator
from django.forms import ModelForm, TextInput, EmailInput, NumberInput
from django import forms
from cassa_massa.web.models import Contact
from cassa_massa.web.validators import validate_only_letters_and_spaces


# class ContactForm(forms.Form):
#     class Meta:
#         model = Contact
#         fields = '__all__'
#
#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass

class ContactForm(forms.ModelForm):
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
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'subject': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Subject'
            }),
            'message': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 700px;',
                'placeholder': 'Message'
            }),
        }

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
