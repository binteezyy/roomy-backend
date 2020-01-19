from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

from django.urls import path,include
from django.conf.urls.static import static
from ..views import *

urlpatterns = [
    #navigation

    path('', landing.home, name='home'),
    path('login/',auth.login, name='login'),
    path('logout/', auth.logout, name='logout'),
    path('booking_guide/', landing.booking_guide, name='booking_guide'),
    path('partner_with_us/', landing.partner_with_us, name='partner_with_us'),
    path('about/', landing.about, name='about'),
    path('faq/', landing.faq, name='faq'),
    path('contact/', landing.contact, name='contact'),
    path('terms_of_use/', landing.terms_of_use, name='terms_of_use'),
    path('privacy/', landing.privacy, name='privacy'),
    path('help_center/', landing.help_center, name='help_center'),
    #property
    path('explore/', explore.index, name='explore'),
    path('explore/property/', property.property, name='property'),
    path('explore/property/room/<int:pk>', explore.room_view, name='room'),
    path('explore/property/amenities', property.amenities, name='amenities'),
    path('explore/property/photos', property.photos, name='photos'),
    path('explore/property/room/booking', property.booking, name='booking'),
]
