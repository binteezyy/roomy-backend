from django.urls import path,include
from django.conf.urls.static import static
from .views import base
urlpatterns = [
    path('explore/', base.explore, name='explore'),
    path('how_to_book/', base.how_to_book, name='how_to_book'),
    path('partner_with_us/', base.partner_with_us, name='partner_with_us'),
    path('about/', base.about, name='about'),
    path('faq/', base.faq, name='faq'),
    path('contact/', base.contact, name='contact'),
    path('terms_of_use/', base.terms_of_use, name='terms_of_use'),
    path('privacy/', base.privacy, name='privacy'),
    path('help_center/', base.help_center, name='help_center'),
]
