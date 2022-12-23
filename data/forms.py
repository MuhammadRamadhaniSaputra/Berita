from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Berita

class BeritaForms(forms.ModelForm):
    class Meta:
        model = Berita
        fields = ('title', 'description', 'kategori' )
        widgets = {
            "title" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':"Title",
                    'type':'text',
                    'required':True
                }),
                "description" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'cols':'30',
                    'rows':'10',
                    'required':True,
                }),
                "kategori" : forms.Select(
                attrs={
                    'class': 'selectpicker',
                    'type':'text',
                    'required':True,
                    'data-style':'btn btn-danger btn-block',
                    'title':'Pilih Kategori',
                    'data-size':'7'
                }),
                
        }