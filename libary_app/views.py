from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import View, TemplateView, ListView, DetailView
# Create your views here.
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.utils import timezone

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import *
from .models import *


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})
    
# Create your views here.
def index(request):
    EN = Book.objects.all().filter(language='EN').count()
    AR = Book.objects.all().filter(language='عربي').count()
    book = Book.objects.all().order_by('-created_dt')[:4]
    TOTAL_BOOK = Book.objects.all().count()
    cat = category.objects.all()
    notify_counts = request.session.get(request.user)
    s_viwes = site_viwes.objects.all().count()
    if not request.session.get(notify_counts,False):
        site_viwes.objects.create(views = 1 )
    return render(request, 'index.html' ,   {'book':book , 'cat':cat , 's_viwes':s_viwes , 'EN':EN ,'AR':AR , 'TOTAL':TOTAL_BOOK} )

def slider(request):
    book = Book.objects.all().order_by('-created_dt')[:4]
    return render(request, 'slider.html' , {'book':book})

class categoryCreateView(BSModalCreateView):
    template_name = 'patient_pso/form.html'
    form_class = category
    success_message = 'تم إضافة القسم بنجاح '
    success_url = reverse_lazy('libary_app:index')

def category_isbn(request,isbn_id):
    title = category.objects.filter(id=isbn_id)
    book= Book.objects.filter(category=isbn_id)
    #cat = Book.objects.filter(category__id = book)
    return render(request,'category_isbn.html',{'cat':book , 'tit':title})



class scoole_appoitment_View( CreateView):
    model = scoole_appoitment
    form_class = scoole_appoitmentForm
    template_name = 'scoole_appoitment.html'
    success_url = reverse_lazy('libary_app:index')

class book_create_view( CreateView):
    model = Book
    form_class = Book_Create_Form
    template_name = 'create_book.html'
    success_message = 'تم إضافة الكتاب بنجاح  '
    success_url = reverse_lazy('libary_app:index')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_by = self.request.user
        post.save()
        return redirect('libary_app:index')

class category_create_view( CreateView):
    model = category
    form_class = category_Create_Form
    template_name = 'create_catgory.html'
    success_message = 'تم إضافة  القسم بنجاح  '
    success_url = reverse_lazy('libary_app:index')

class scoole_appoiment_list_view( ListView):
    model = scoole_appoitment
    context_object_name = 'school'
    template_name = 'school_appoitment_list_view.html'


class teamt_list_view( ListView):
    model = project_team
    context_object_name = 'team'
    template_name = 'team_list_view.html'


class bookDetailView(DetailView , UpdateView):
    template_name = 'book_detail.html'
    model = Book
    context_object_name = 'book'

def bookDetail_View(request,pk):
    book = get_object_or_404(Book,pk=pk)
    session_key = 'view_book_{}'.format(book.pk)
    if not request.session.get(session_key,False):
        book.views +=1
        book.save()
        request.session[session_key] = False

    return render(request,'book_detail.html',{'book':book})