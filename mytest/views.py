from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_name = "front/index.html"
    context = {
        'title':'Home',

    }
    return render(request, template_name, context)

def about(request):
    template_name = "front/about.html"
    context = {
        'title':'About',

    }
    return render(request, template_name, context)

def login(request):
    template_name = "front/login.html"
    context = {
        'title':'',

    }
    return render(request, template_name, context)
