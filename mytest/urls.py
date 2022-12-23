from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('blog_page/', blog_page, name='blog_page'),
    path('single_news/', single_news, name='single_news'),
    path('detail_news/<str:id>', detail_news, name='detail_news'),
    path('dasbord/', include('data.urls')),
    path('logout/', logout_view, name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)