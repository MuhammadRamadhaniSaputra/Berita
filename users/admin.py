from django.contrib import admin
from .models import Biodata
# Register your models here.

class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user','telp')
admin.site.register(Biodata, BiodataAdmin)