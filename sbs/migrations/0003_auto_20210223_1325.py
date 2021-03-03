# Generated by Django 2.2.6 on 2021-02-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sbs', '0002_auto_20210223_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abirimparametre',
            name='type',
            field=models.CharField(choices=[('date', 'Date'), ('string', 'String'), ('number', 'Number')],
                                   default='string', max_length=128, verbose_name='Türü '),
        ),
    ]
