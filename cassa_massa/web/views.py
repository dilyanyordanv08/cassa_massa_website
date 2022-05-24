from django.contrib import messages
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView, ListView, DetailView

from cassa_massa.web.forms import ContactForm, TableInquiryForm
from cassa_massa.web.models import Services, FinishedProducts, Images, Post, Reviews


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


class TableCategoryListView(ListView):
    model = Images
    template_name = 'main/proekti/tables.html'
    context_object_name = 'category_images'

    queryset = Images.objects.filter(category__category_title="tables")


class TablesDetailView(DetailView):
    model = Images
    template_name = "main/proekti/tables_slug.html"
    context_object_name = 'image'


class KitchenCategoryListView(ListView):
    model = Images
    template_name = 'main/proekti/kitchens.html'
    context_object_name = 'category_images'

    queryset = Images.objects.filter(category__category_title="kitchens")


class KitchenDetailView(DetailView):
    model = Images
    template_name = "main/proekti/kitchens-slug.html"
    context_object_name = 'image'


class BedroomCategoryListView(ListView):
    model = Images
    template_name = 'main/proekti/bedroom.html'
    context_object_name = 'category_images'

    queryset = Images.objects.filter(category__category_title="bedrooms")


class BedroomDetailView(DetailView):
    model = Images
    template_name = "main/proekti/bedroom-slug.html"
    context_object_name = 'image'


class WardrobesCategoryListView(ListView):
    model = Images
    template_name = 'main/proekti/wardrobes.html'
    context_object_name = 'category_images'

    queryset = Images.objects.filter(category__category_title="wardrobes")


class WardrobesDetailView(DetailView):
    model = Images
    template_name = "main/proekti/wardrobes-slug.html"
    context_object_name = 'image'


class OthersCategoryListView(ListView):
    model = Images
    template_name = 'main/proekti/others.html'
    context_object_name = 'category_images'

    queryset = Images.objects.filter(category__category_title="others")


class OthersDetailView(DetailView):
    model = Images
    template_name = "main/proekti/others-slug.html"
    context_object_name = 'image'


class BlogPostView(ListView):
    model = Post
    template_name = 'main/blog/blog.html'


class BlogPostDetailView(DetailView):
    model = Post
    template_name = "main/blog/blog-01.html"


class ReviewsListview(ListView):
    model = Reviews
    template_name = 'index.html'
    context_object_name = 'firm_reviews'


def internal_error(request):
    return HttpResponse('An error occurred, please  try again')


class InternalErrorView(View):
    def get(self, request):
        return HttpResponse('An error occurred, please  try again')
