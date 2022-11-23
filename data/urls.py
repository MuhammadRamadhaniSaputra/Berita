from django.urls import path, include
from data.views import *

urlpatterns = [
    #path('',dasbord, name='dasbord'),
    path('',artikel, name='tabel_artikel'),
    path('users',users, name='tabel_users'),
    path('list', list_mahasiswa, name='list_mahasiswa'),
    path('tambah', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('update/<int:id>', update_mahasiswa, name='update_mahasiswa'),
    path('delete/<int:id>', delete_mahasiswa, name='delete_mahasiswa'),
]
