from django.urls import path
from django.views.generic import TemplateView

from cassa_massa.web.views import ContactFormCreateView, ServicesListView

urlpatterns = (
    path('privacy-policy/', TemplateView.as_view(template_name='main/privacy_policy.html')),
    # path('contacts/', contact_view, name='contacts'),

    path('contacts/', ContactFormCreateView.as_view(), name='contacts'),

    path('services/', ServicesListView.as_view(), name='services'),


)
