from django.urls import path,include
from django.conf.urls.static import static
from .views import base
urlpatterns = [
    path('', base.index, name='index'),
    path('explore/', base.explore, name='explore'),
    path('about/', base.about, name='about'),
    path('faq/', base.faq, name='faq'),
]
