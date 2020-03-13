from django.contrib import admin
from django.contrib.admin import AdminSite
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


class ClientAdmin(AdminSite):
    name        = "client_admin"
    site_header = "Roomy — Client"
    site_title  = "Roomy — Client"
    index_title = "Manage the client web-app here"

class CoreAdmin(AdminSite):
    site_header = "Roomy — Core"
    site_title  = "Roomy — Core"
    index_title = "Manage the core web-app here"

core_admin = CoreAdmin(name='core_admin')
client_admin = ClientAdmin(name='client_admin')

urlpatterns = [
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
