# Generated by Django 2.2.6 on 2021-02-26 17:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sbs', '0014_auto_20210226_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aevrak',
            name='name',
        ),
    ]
