from django.urls import path
from django.views.generic import TemplateView

from cassa_massa.web.views import ContactFormCreateView, ServicesListView, FinishedProductsListView, \
    TableInquiryCreateView, TableCategoryListView, KitchenCategoryListView, BedroomCategoryListView, \
    WardrobesCategoryListView, OthersCategoryListView, BlogPostView, BlogPostDetailView, TablesDetailView, \
    BedroomDetailView, KitchenDetailView, WardrobesDetailView, OthersDetailView

urlpatterns = (
    path('privacy-policy/', TemplateView.as_view(template_name='main/privacy_policy.html')),

    path('proekti/masi/', TableCategoryListView.as_view(), name='tables'),
    path('proekti/masi/<slug:slug>', TablesDetailView.as_view(), name='table-details'),

    path('proekti/kuhni/', KitchenCategoryListView.as_view(), name='kitchens'),
    path('proekti/kuhni/<slug:slug>', KitchenDetailView.as_view(), name='kitchens-details'),

    path('proekti/spalni/', BedroomCategoryListView.as_view(), name='bedrooms'),
    path('proekti/spalni/<slug:slug>', BedroomDetailView.as_view(), name='bedrooms-details'),

    path('proekti/garderobi/', WardrobesCategoryListView.as_view(), name='wardrobes'),
    path('proekti/garderobi/<slug:slug>', WardrobesDetailView.as_view(), name='wardrobes-details'),

    path('proekti/others/', OthersCategoryListView.as_view(), name='others'),
    path('proekti/others/<slug:slug>', OthersDetailView.as_view(), name='others-details'),

    path('blog/', BlogPostView.as_view(), name='blogs-list'),
    path('blog/<slug:slug>', BlogPostDetailView.as_view(), name='article-detail'),

    path('finished-products/', FinishedProductsListView.as_view(), name='finished-products'),
    path('contacts/', ContactFormCreateView.as_view(), name='contacts'),
    path('materials/', TemplateView.as_view(template_name='main/materials.html'), name='materials'),
    path('services/', ServicesListView.as_view(), name='services'),
    path('table-inquiry/', TableInquiryCreateView.as_view(), name='table-inquiry-form'),
)
