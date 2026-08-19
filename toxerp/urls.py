"""
URL configuration for toxerp project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    # Redirect legacy asset/page requests to the static URL so old HTML works without edits
    path('assets/<path:path>', RedirectView.as_view(url='/static/assets/%(path)s', permanent=False)),
    path('pages/<path:path>', RedirectView.as_view(url='/static/pages/%(path)s', permanent=False)),

    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    # Serve the repository's index.html at the site root
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # Add ERP app URLs when ready, e.g.:
    # path('api/erp/', include('erp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # In debug only: optionally serve static files from STATIC_ROOT (dev convenience)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
