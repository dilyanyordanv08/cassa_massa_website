from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, ListView

from cassa_massa.web.forms import ContactForm

#
# def contact_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'main/contacts.html')
#     form = ContactForm()
#     context = {'form': form}
#     return render(request, 'main/contacts.html', context)
from cassa_massa.web.models import Services


class ServicesTemplateView(TemplateView):
    template_name = 'main/services.html'


# class ContactFormCreateView(CreateView):
#     template_name = 'main/contacts.html'
#     form_class = ContactForm()
#     success_url = reverse_lazy('contacts')

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

