from django.urls import path
from django.views.generic import TemplateView

from cassa_massa.web.views import PrivacyPolicyTemplateView

urlpatterns = (
    path('privacy-policy/', TemplateView.as_view(template_name='privacy_policy.html')),
)