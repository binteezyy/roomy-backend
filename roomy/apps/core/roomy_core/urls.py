from django.urls import path,include
from django.conf.urls.static import static
from .views import base

from .views import api_views
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('properties', api_views.PropertyApiView)
router.register('fees', api_views.FeeApiView)
router.register('billings', api_views.BillingApiView)
router.register('catalogs', api_views.RoomCatalogApiView)
router.register('rooms', api_views.RoomApiView)
router.register('messages', api_views.MessageApiView)
router.register('tenants', api_views.TenantAccountApiView)
router.register('guests', api_views.GuestApiView)
router.register('images', api_views.ImageFileApiView)
router.register('owners', api_views.OwnerAccountApiView)
router.register('users', api_views.UserApiView)
router.register('transactions', api_views.TransactionApiView)
router.register('requests', api_views.RequestApiView)
router.register('messages', api_views.MessageApiView)
# filtered routers
router.register(r'rooms-in-property/(?P<property_id>[0-9]+)', api_views.RoomCatalogInPropertyApiView, basename='rooms-in-property')
router.register(r'rooms-in-location/(?P<location>.+)', api_views.RoomCatalogInLocationApiView, basename='rooms-in-location')
router.register(r'rooms-filter/(?P<search_query>.+)', api_views.RoomCatalogFilterApiView, basename='rooms-filter')

urlpatterns = [
    path('index/',      base.index,                                        name='api-index'),
    path('', include(router.urls)),
    path('test/', base.test_script, name='test-script'),
    path('token-auth/', views.obtain_auth_token, name='token-auth'),
]
