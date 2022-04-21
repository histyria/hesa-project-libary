from django.contrib import admin
from django.urls import path , include
from .views import *
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

app_name = 'libary_app'
urlpatterns = [
    path('',index,name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)