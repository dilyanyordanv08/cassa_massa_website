from django.urls import path
from django.views.generic import TemplateView

from cassa_massa.web.views import ContactFormCreateView, ServicesListView, FinishedProductsListView, \
    TableInquiryCreateView, TableCategoryListView, KitchenCategoryListView, BedroomCategoryListView, \
    WardrobesCategoryListView, OthersCategoryListView

urlpatterns = (
    path('privacy-policy/', TemplateView.as_view(template_name='main/privacy_policy.html')),
    # path('contacts/', contact_view, name='contacts'),

    path('finished-products/', FinishedProductsListView.as_view(), name='finished-products'),
    path('contacts/', ContactFormCreateView.as_view(), name='contacts'),
    path('materials/', TemplateView.as_view(template_name='main/materials.html'), name='materials'),
    path('services/', ServicesListView.as_view(), name='services'),

    path('table-inquiry/', TableInquiryCreateView.as_view(), name='table-inquiry-form'),

    path('proekti/masi/', TableCategoryListView.as_view(), name='tables'),
    path('proekti/kuhni/', KitchenCategoryListView.as_view(), name='kitchens'),
    path('proekti/spalni/', BedroomCategoryListView.as_view(), name='bedrooms'),
    path('proekti/garderobi/', WardrobesCategoryListView.as_view(), name='wardrobes'),
    path('proekti/others/', OthersCategoryListView.as_view(), name='others'),


)
