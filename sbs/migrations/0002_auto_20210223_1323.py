# Generated by Django 2.2.6 on 2021-02-23 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adosyaparametre',
            name='type',
            field=models.CharField(choices=[('date', 'Date'), ('string', 'String'), ('number', 'Number')], default='string', max_length=128, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='aklasor',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sbs.CategoryItem'),
        ),
        migrations.DeleteModel(
            name='Alocation',
        ),
    ]
