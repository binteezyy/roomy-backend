from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('roomy_admin.urls')),
    path('core/', include('roomy_core.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

admin.site.site_header = "Roomy Client"
admin.site.site_title = "Roomy Client Portal"
admin.site.index_title = "Welcome to Roomy Admin Portal"
