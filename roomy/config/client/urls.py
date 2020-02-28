from django.urls import path, include
from django.contrib.auth import logout
from ..common import urlpatterns
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns += [
    path('', include('apps.client.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('social-close/',TemplateView.as_view(template_name="web/components/_close.html"), name="social-close")
]

if settings.DEBUG:
    from django.contrib import admin
    urlpatterns += [path('admin/', admin.site.urls),]
