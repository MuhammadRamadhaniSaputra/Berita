from django.urls import path, include
from data.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',dasbord, name='dasbord'),
    path('artikel/',artikel, name='tabel_artikel'),
    path('tambah_artikel/',tambah_artikel, name='tambah_artikel'),
    path('users',users, name='tabel_users'),
    path('delete/<str:id>', delete_artikel, name='delete_artikel'),
    path('detail/<str:id>', liat_artikel, name='liat_artikel'),
    path('edit/<str:id>', edit_artikel, name='edit_artikel'),
    # path('',api,name='api')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
