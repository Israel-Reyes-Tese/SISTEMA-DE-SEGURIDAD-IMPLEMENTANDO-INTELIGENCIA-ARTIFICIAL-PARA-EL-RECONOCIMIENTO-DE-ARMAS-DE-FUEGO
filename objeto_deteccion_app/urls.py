from django.urls import path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import detect_objects, video_feed


urlpatterns = [
    path('detect/', detect_objects, name='detect_objects'),
    path('video_feed/', video_feed, name='video_feed')

]