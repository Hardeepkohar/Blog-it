from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category),
]