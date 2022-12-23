from tabnanny import check
from unicodedata import name
from django.shortcuts import redirect, render
from data.models import *
import requests
from django.contrib.auth.decorators import login_required
from .forms import BeritaForms
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Create your views here.

def id_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def dasbord(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'
        
    template_name = "back/dasbord.html"
    context = {
        'title':'tabel artikel',
    }
    return render(request, template_name, context)

def base(request):
    template_name = "front/home.html"
    list_berita = Berita.objects.all()
    context = {
        'title':'Home',
        'berita':list_berita

    }
    return render(request, template_name, context)


def delete_artikel(request, id):
    Berita.objects.get(id=id).delete()
    return redirect(artikel)


@login_required
def artikel(request):
    template_name = "back/table_artikel.html"
    artikel = Berita.objects.all()
    context = {
        'title':'tabel artikel',
        'artikel':artikel,
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        forms_artikel = BeritaForms(request.POST)
        if forms_artikel.is_valid():
            forms_artikel.save()
        return redirect(artikel)
    else:
        forms_artikel = BeritaForms()
    context = {
        'title':'tambah artikel',
        'kategori' :kategori,
        'forms_artikel':forms_artikel
    }
    return render(request, template_name, context)

def liat_artikel(request, id):
    template_name = "back/liat_artikel.html"
    artikel= Berita.objects.get(id=id)
    context = {
        'title':'lihat artikel',
        'artikel': artikel,

    }
    return render(request, template_name, context)

def edit_artikel(request, id):
    template_name = "back/tambah_artikel.html"
    q = Berita.objects.get(id=id)
    if request.method == "POST":
        forms_artikel = BeritaForms(request.POST,instance=q)
        if forms_artikel.is_valid():
            forms_artikel.save()
        return redirect(artikel)
    else:
        forms_artikel = BeritaForms(instance=q)
    context = {
        'title':'halaman edit',
        'artikel': q,
        'forms_artikel' :forms_artikel
    }
    return render(request, template_name, context)


@login_required
@user_passes_test(id_operator)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title':'tabel users',
        'list_user': list_user

    }
    return render(request, template_name, context)



def api(request):
    response=request.get('https://newsapi.org/v2/top-headlines?country=id&apiKey=60adcaea2f2b4b109fcd70ea9be1091e').json()
    return render(request,'home.html',{'response':response})