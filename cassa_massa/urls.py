from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('cassa_massa.auth_app.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='base'),

    path('', include('cassa_massa.web.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

