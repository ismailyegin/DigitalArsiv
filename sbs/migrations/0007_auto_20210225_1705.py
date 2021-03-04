# Generated by Django 2.2.6 on 2021-02-25 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0006_auto_20210225_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='adosya',
            name='name',
            field=models.CharField(default=1, max_length=120, verbose_name='Tanımı'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aklasor',
            name='birim',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sbs.Abirim', verbose_name='Birim'),
        ),
        migrations.AlterField(
            model_name='aklasor',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Tanımı'),
        ),
    ]
