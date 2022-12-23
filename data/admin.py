from django.contrib import admin
from data.models import *
# Register your models here.
admin.site.register(Kategori)
# class ProdukAdmin(admin.ModelAdmin):
#     list_display = ['nama', 'nim', 'prodi', 'angkatan']
# admin.site.register(Mahasiswa, ProdukAdmin)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'kategori', 'image', 'date']
admin.site.register(Berita, BeritaAdmin)
