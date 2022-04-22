from django.urls import path
from django.views.generic import TemplateView

from cassa_massa.web.views import ContactFormCreateView, ServicesListView, FinishedProductsListView, \
    TableInquiryCreateView, ImageCategoryListView

urlpatterns = (
    path('privacy-policy/', TemplateView.as_view(template_name='main/privacy_policy.html')),
    # path('contacts/', contact_view, name='contacts'),

    path('finished-products/', FinishedProductsListView.as_view(), name='finished-products'),
    path('contacts/', ContactFormCreateView.as_view(), name='contacts'),
    path('materials/', TemplateView.as_view(template_name='main/materials.html'), name='materials'),
    path('services/', ServicesListView.as_view(), name='services'),

    path('table-inquiry/', TableInquiryCreateView.as_view(), name='table-inquiry-form'),

    path('proekti/masi/', ImageCategoryListView.as_view(), name='tables'),

)
