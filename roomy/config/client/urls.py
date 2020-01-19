from django.urls import path, include
from django.contrib.auth import logout
from ..common import urlpatterns
from django.conf import settings

urlpatterns += [
    path('', include('apps.client.urls')),
    path('', include('social_django.urls', namespace='social')),

]

if settings.DEBUG:
    from django.contrib import admin
    urlpatterns += [path('admin/', admin.site.urls),]
