from django.contrib import admin
from data.models import *
# Register your models here.
admin.site.register(Angkatan)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nim', 'prodi', 'angkatan']
admin.site.register(Mahasiswa, ProdukAdmin)
