from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('cassa_massa.auth_app.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='base'),

    path('', include('cassa_massa.web.urls')),

]
