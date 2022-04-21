
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from libary_app import views
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    path('', include('libary_app.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)