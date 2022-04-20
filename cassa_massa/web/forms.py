from django.forms import TextInput, EmailInput
from django import forms
from cassa_massa.web.models import Contact, TableContactForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'cell_phone_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Telephone Number'
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 700px;',
                'placeholder': 'Message'
            }),
        }

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass


class TableInquiryForm(forms.ModelForm):
    class Meta:
        model = TableContactForm
        fields = '__all__'

        widgets = {
            'table_type': forms.Select(attrs={
                'style': 'width: 160px',
            }),

            'number_of_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 50px',
            }),

            'table_shape': forms.Select(attrs={
                'style': 'width: 160px',
            }),

            'table_arrangement': forms.Select(attrs={
                'style': 'width: 160px',
            }),

            'wood_type': forms.Select(attrs={
                 'style': 'width: 160px',
            }),

            'table_epoxy_color': forms.Select(attrs={
                'style': 'width: 160px',
            }),

            'table_legs': forms.Select(attrs={
                 'style': 'width: 160px',
            }),

            'table_top_oil': forms.Select(attrs={
                 'style': 'width: 160px',
            }),

            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Име',
                'style': 'width: 500px',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'style': 'width: 500px',
            }),

            'cell_phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telephone number',
                'style': 'width: 500px',
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'rows': '3',
                'style': 'width: 500px',
            }),

        }

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
