# Generated by Django 2.2.6 on 2021-02-25 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0003_auto_20210223_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abirimparametre',
            name='birim',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sbs.Abirim', verbose_name='Birim'),
        ),
        migrations.AlterField(
            model_name='abirimparametre',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Başlık'),
        ),
    ]
