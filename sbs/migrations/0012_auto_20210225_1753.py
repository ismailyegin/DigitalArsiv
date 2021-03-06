# Generated by Django 2.2.6 on 2021-02-25 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0011_remove_adosyaparametre_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adosyaparametre',
            name='dosya',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sbs.Adosya'),
        ),
        migrations.AlterField(
            model_name='adosyaparametre',
            name='parametre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sbs.AbirimParametre'),
        ),
    ]
