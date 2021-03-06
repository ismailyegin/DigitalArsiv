# Generated by Django 2.2.6 on 2021-02-25 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0005_auto_20210225_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aklasor',
            name='birim',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sbs.Abirim', verbose_name='Birim:'),
        ),
        migrations.AlterField(
            model_name='aklasor',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sbs.CategoryItem', verbose_name='Konumu'),
        ),
        migrations.AlterField(
            model_name='aklasor',
            name='name',
            field=models.CharField(default=1, max_length=120, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aklasor',
            name='sirano',
            field=models.IntegerField(default=1, verbose_name='Sıra Numarası'),
            preserve_default=False,
        ),
    ]
