# Generated by Django 4.1.1 on 2022-10-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_rename_prdi_mahasiswa_prodi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='prodi',
            field=models.CharField(max_length=30),
        ),
    ]
