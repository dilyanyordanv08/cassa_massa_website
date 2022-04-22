from django.contrib import messages
from django.views.generic import FormView, ListView

from cassa_massa.web.forms import ContactForm, TableInquiryForm
from cassa_massa.web.models import Services, FinishedProducts, Category, Images


class ContactFormCreateView(FormView):
    template_name = 'main/contacts.html'
    form_class = ContactForm
    success_url = 'main/contacts.html'

    # TODO
    # Method is called when valid form data has been POSTed, should return HttpResponse
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Message was sent successfully!")


class ServicesListView(ListView):
    model = Services
    template_name = 'main/services.html'
    context_object_name = 'services'
    description_items = Services.objects.all().order_by('description')


class FinishedProductsListView(ListView):
    model = FinishedProducts
    template_name = 'main/ready-to-sell-products.html'
    context_object_name = 'finished_products'


class TableInquiryCreateView(FormView):
    template_name = 'main/table_inquiry_form.html'
    form_class = TableInquiryForm
    # success_url = 'table-inquiry'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Message was sent successfully!")


class ImageCategoryListView(ListView):
    model = Images
    template_name = 'main/proekti/masi.html'
    context_object_name = 'images'
    description_items = Images.objects.all().order_by('title')



