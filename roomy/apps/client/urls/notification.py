from django.urls import path,include
from ..views.notification import *

notification_urls = [
    path('demo/', demo, name='webpush-demo'),
]
