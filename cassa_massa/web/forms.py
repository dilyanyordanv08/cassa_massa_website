from django.forms import TextInput, EmailInput
from django import forms
from cassa_massa.web.models import Contact, TableContactForm


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


class TableInquiryForm(forms.ModelForm):
    class Meta:
        model = TableContactForm
        fields = '__all__'

        widgets = {
            'table_type': forms.RadioSelect(),

            'number_of_seats': forms.NumberInput(attrs={'style': 'width: 50px'}),

            'table_shape': forms.RadioSelect(),

            'table_arrangement': forms.RadioSelect(),

            'wood_type': forms.RadioSelect(),

            'table_epoxy_color': forms.RadioSelect(),

            'table_legs': forms.RadioSelect(),

            'table_top_oil': forms.RadioSelect(),

            'customer_name': forms.TextInput(),

            'email': forms.EmailInput(),

            'cell_phone_number': forms.TextInput(),

            'message': forms.Textarea(),



        }

    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary
    #     pass
