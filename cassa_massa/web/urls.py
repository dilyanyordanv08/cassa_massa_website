from django.urls import path
from django.views.generic import TemplateView

from cassa_massa.web.views import contact_view

urlpatterns = (
    path('privacy-policy/', TemplateView.as_view(template_name='main/privacy_policy.html')),
    path('contacts/', contact_view, name='contacts'),
)
