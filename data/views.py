from tabnanny import check
from unicodedata import name
from django.shortcuts import redirect, render
from data.models import *

# Create your views here.
def list_mahasiswa(request):
    template_name = "front/list_mahasiswa.html"
    list_mahasiswa = Mahasiswa.objects.all()
    context = {
        'title':'halaman list mahasiswa',
        'mahasiswa':list_mahasiswa

    }
    return render(request, template_name, context)

def tambah_mahasiswa(request):
    template_name = "front/tambah_mahasiswa.html"
    angkatan = Angkatan.objects.all()
    if request.method == "POST":

        input_nama = request.POST.get('nama')
        input_nim = request.POST.get('nim')
        input_prodi = request.POST.get('prodi')
        input_angkatan= request.POST.get('angkatan')

        get_angkatan = Angkatan.objects.get(nama=input_angkatan)

        Mahasiswa.objects.create(
            nama = input_nama,
            nim = input_nim,
            prodi = input_prodi,
            angkatan = get_angkatan,
        )
        return redirect(list_mahasiswa)

    context = {
        'title':'ini adalah halaman tambah mahasiswa',
        'angkatan':angkatan
    }
    return render(request, template_name, context)


def update_mahasiswa(request, id):
    template_name = "front/tambah_mahasiswa.html"
    angkatan = Angkatan.objects.all()
    get_mahasiswa = Mahasiswa.objects.get(id=id)
    if request.method == "POST":

        input_nama = request.POST.get('nama')
        input_nim = request.POST.get('nim')
        input_prodi = request.POST.get('prodi')
        input_angkatan= request.POST.get('angkatan')

        get_angkatan = angkatan.objects.get(nama=input_angkatan)

        get_mahasiswa.nama = input_nama
        get_mahasiswa.nim = input_nim
        get_mahasiswa.prodi = input_prodi
        get_mahasiswa.angkatan = get_angkatan
        get_mahasiswa.save()
        return redirect(list_mahasiswa)

    context = {
        'title':'ini adalah halaman tambah barang',
        'angkatan':angkatan,
        'get_mahasiswa': get_mahasiswa
    }
    return render(request, template_name, context)

def delete_mahasiswa(request, id):
    Mahasiswa.objects.get(id=id).delete()
    return redirect(list_mahasiswa)

def artikel(request):
    template_name = "back/table_artikel.html"
    artikel = Mahasiswa.objects.all()
    # for a in artikel:
    #     print(a)
    context = {
        'title':'tabel artikel',
        'artikel':artikel,
    }
    return render(request, template_name, context)

def users(request):
    template_name = "back/tabel_users.html"
    context = {
        'title':'tabel users',

    }
    return render(request, template_name, context)
