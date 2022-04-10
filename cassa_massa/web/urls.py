from django.urls import path
from django.views.generic import TemplateView

urlpatterns = (
    path('privacy-policy/', TemplateView.as_view(template_name='main/privacy_policy.html')),
    path('contacts/', TemplateView.as_view(template_name='main/contacts.html')),
)
