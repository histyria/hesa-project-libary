from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    book = Book.objects.all()
    return render(request, 'index.html' , {'book':book})