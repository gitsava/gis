# Generated by Django 2.2.1 on 2019-07-22 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0003_auto_20180109_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akun',
            name='akun',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='akun',
            name='pegawai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pegawai.Pegawai'),
        ),
        migrations.AlterField(
            model_name='pegawai',
            name='jabatan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pegawai', to='pegawai.Jabatan'),
        ),
    ]
