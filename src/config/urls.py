from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app.internal.urls import urlpatterns as rest_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('app.internal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + rest_urls
