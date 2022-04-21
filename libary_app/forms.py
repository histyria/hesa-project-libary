from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class categoryModelForm(BSModalModelForm):
    class Meta:
        model = category
        fields = ['category']
class scoole_appoitmentForm(forms.ModelForm):
    
    
    class Meta:
        model = scoole_appoitment
        fields = '__all__'
        exclude = ('created_dt' ,)
        widgets = {
    'appoitment_dt': forms.DateInput( format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'الرجاء إختيار التاريخ' , 'type': 'date' }),}


class Book_Create_Form(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'عنوان الكتاب'
        self.fields['summary'].widget.attrs['placeholder'] = 'نبذة مختصرة عن الكتاب'
        self.fields['author'].widget.attrs['placeholder'] = 'إسم المؤلف'
        self.fields['category'].widget.attrs['placeholder'] = 'category'
        self.fields['language'].widget.attrs['placeholder'] = 'لغة الكتاب'
    class Meta:
        model = Book
        exclude = ('views', 'created_by' , 'created_dt' )
        fields = '__all__'
   

class category_Create_Form(forms.ModelForm):
    
    class Meta:
        model = category
        fields = '__all__'