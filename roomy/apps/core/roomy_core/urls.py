from django.urls import path,include
from django.conf.urls.static import static
from .views import base

from .views import api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('properties', api_views.PropertyApiView)
router.register('rooms', api_views.RoomApiView)
router.register('fees', api_views.FeeApiView)
router.register('billings', api_views.BillingApiView)
router.register('messages', api_views.MessageApiView)
router.register('tenants', api_views.TenantAccountApiView)
router.register('guests', api_views.GuestApiView)
urlpatterns = [
    path('index/',      base.index,                                        name='api-index'),
    path('', include(router.urls))
]
