from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=40)
    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Kategori"

class Berita(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(blank=True, null=True, 
                                        config_name='special',
                                        external_plugin_resources=[(
                                            'youtube',
                                            '/static/ckeditor_plugins/youtube/youtube/',
                                            'plugin.js',
                                            )],
                                        )
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return "{} - {} - {}".format(self.title, self.description, self.image)

    class Meta:
        verbose_name_plural = "Berita"