from django.db import models

# Create your models here.

class Angkatan(models.Model):
    nama = models.CharField(max_length=40)
    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Angkatan"

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    prodi = models.CharField(max_length=30)
    angkatan = models.ForeignKey(Angkatan, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.nama, self.nim, self.prodi, self.angkatan)

    class Meta:
        verbose_name_plural = "Mahasiswa"