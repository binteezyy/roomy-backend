from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.client.urls')),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

admin.site.site_header = "Roomy Admin"
admin.site.site_title = "Roomy Admin Portal"
admin.site.index_title = "Welcome to Roomy Admin Portal"
