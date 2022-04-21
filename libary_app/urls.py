from django.urls import path, include , re_path
from .views import *
from django.conf.urls import url 
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.views.static import serve

app_name = 'libary_app'

urlpatterns = [
path('',index,name='index'),
path('admin/', admin.site.urls ,name='admin'),
path('isbn/<int:isbn_id>/',category_isbn,name='category_isbn'),
path('create/', categoryCreateView.as_view(), name='categoryCreateView'),
path('school/', scoole_appoitment_View.as_view(), name='scoole_appoitment_View'),
path('book/create/', book_create_view.as_view(), name='book_create_view'),
path('category/create/', category_create_view.as_view(), name='category_create_view'),
path('school/appoitement/', scoole_appoiment_list_view.as_view(), name='scoole_appoiment_list_view'),
path('team/', teamt_list_view.as_view(), name='teamt_list_view'),
path('book/<int:pk>/',bookDetail_View, name='bookDetailView'),
]
