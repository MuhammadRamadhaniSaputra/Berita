from django.contrib import admin
from data.models import *
# Register your models here.
admin.site.register(Kategori)

class BeritaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'title', 'description', 'kategori', 'date']
admin.site.register(Berita, BeritaAdmin)
