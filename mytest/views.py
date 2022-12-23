from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponse
from data.models import *
import requests
from data.forms import BeritaForms
from users.models import Biodata
from django.contrib.auth.models import User
from django.db import  transaction
from django.contrib.auth.hashers import make_password

# def home(request):
#     template_name = "front/home.html"
#     list_berita = Berita.objects.all()
#     context = {
#         'title':'Home',
#         'berita':list_berita

#     }
#     return render(request, template_name, context)



def contact(request):
    template_name = "front/contact.html"
    context = {
        'title':'contact',

    }
    return render(request, template_name, context)


def login(request):
    if request.user.is_authenticated:
        print('sudah login')
        return redirect('home')
    template_name = "account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #data benar
            print('username benar')
            auth_login(request, user)
            return redirect('home')
        else:
            #data salah
            print('pasword salah')
    context = {
        'title':'form login',

    }
    return render(request, template_name, context)

def registrasi(request):
    template_name = "account/register.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        telp = request.POST.get('telp')
        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name = nama_belakang,
                    email = email,
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    telp = telp,
                )
            return redirect(home)
        except:pass
    context = {
        'title':'registrasi'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')

def blog_page(request):
    url = "https://newsapi.org/v2/top-headlines?country=id&apiKey=60adcaea2f2b4b109fcd70ea9be1091e"

    data = requests.get(url).json()

    a = data['articles']
    nama = []
    title = []
    desc = []
    tanggal = []
    link = []
    img = []

    for i in range(len(a)):
        f = a[i]
        nama.append(f['author'])
        title.append(f['title'])
        desc.append(f['description'])
        tanggal.append(f['publishedAt'])
        link.append(f['url'])
        img.append(f['urlToImage'])
    
    mylist = zip(title, desc, nama, tanggal,link, img)
    context ={'mylist':mylist}

    return render(request, 'front/blog_page.html', context)

def home(request):
    url = "https://newsapi.org/v2/top-headlines?country=id&apiKey=60adcaea2f2b4b109fcd70ea9be1091e"

    data = requests.get(url).json()

    a = data['articles']
    nama = []
    title = []
    desc = []
    tanggal = []
    link = []
    img = []

    # for i in range(len(a)):
    for i in range(len(a)):
        f = a[i]
        nama.append(f['author'])
        title.append(f['title'])
        desc.append(f['description'])
        tanggal.append(f['publishedAt'])
        link.append(f['url'])
        img.append(f['urlToImage'])
    
    mylist = zip(title, desc, nama, tanggal,link, img)
    w = zip(title, desc, nama, tanggal,link, img)
    q = zip(title, desc, nama, tanggal,link, img)
    context ={
        'mylist':mylist,
        'w':w,
        'q':q
        }
   

    return render(request, 'front/home.html', context)

def single_news(request):
    template_name = "front/single_news.html"
    list_page = Berita.objects.all()
    context = {
        'title':'single_news',
        'post':list_page

    }
    return render(request, template_name, context)

def detail_news(request, id):
    template_name = "front/detail.html"
    artikel = Berita.objects.get(id=id)
    context = {
        'title':'detail_news',
        'detail':artikel

    }
    return render(request, template_name, context)