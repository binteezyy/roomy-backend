from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from ..common import urlpatterns
from apps.core.roomy_core.billing_script import billing_create
import time
urlpatterns += [
    path('api/', include('apps.core.roomy_core.urls')),
    path('', include('apps.core.roomy_admin.urls')),
    path('', include('pwa.urls')),
]

if settings.DEBUG:
    from django.contrib import admin
    urlpatterns += [path('admin/', admin.site.urls), ]
