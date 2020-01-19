from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from ..common import urlpatterns

urlpatterns +=  [
    path('api/', include('apps.core.roomy_core.urls')),
]
