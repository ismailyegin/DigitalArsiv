# Generated by Django 2.2.6 on 2021-02-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0013_auto_20210226_0751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aevrak',
            name='t1',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t10',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t11',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t12',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t13',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t14',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t15',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t16',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t2',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t3',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t4',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t5',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t6',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t7',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t8',
        ),
        migrations.RemoveField(
            model_name='aevrak',
            name='t9',
        ),
        migrations.AddField(
            model_name='aevrak',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abirimparametre',
            name='type',
            field=models.CharField(choices=[('date', 'Date'), ('string', 'String'), ('number', 'Number'), ('file', 'file')], default='string', max_length=128, verbose_name='Türü '),
        ),
    ]
