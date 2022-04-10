from django.forms import ModelForm

from cassa_massa.web.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
