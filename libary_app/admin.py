from django.contrib import admin

# Register your models here.
from .models import *

modler = ( category , Book , project_team)

admin.site.register(modler)