# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrip', models.CharField(max_length=50)),
                ('proratea', models.IntegerField()),
                ('orden', models.IntegerField()),
                ('grupo', models.IntegerField()),
                ('modulo', models.IntegerField()),
                ('topepro', models.IntegerField()),
                ('signo', models.IntegerField()),
                ('concepto', models.CharField(max_length=10)),
                ('grupotope', models.IntegerField()),
                ('muestra_liq', models.IntegerField()),
                ('anexas', models.IntegerField()),
                ('vista', models.IntegerField()),
                ('titulo', models.IntegerField()),
                ('of649', models.CharField(max_length=6)),
                ('ordenliq', models.CharField(max_length=6)),
                ('fliqfin', models.CharField(max_length=6)),
                ('grupolf', models.IntegerField()),
                ('ldescrip', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_emp', models.IntegerField()),
                ('saf', models.IntegerField()),
                ('descrip', models.CharField(max_length=50)),
                ('clave_seg', models.CharField(max_length=50)),
                ('cod_tipo', models.IntegerField()),
                ('excep', models.IntegerField()),
                ('saf_central', models.IntegerField()),
                ('cuit', models.CharField(max_length=13)),
                ('calle', models.CharField(max_length=30)),
                ('nro', models.IntegerField()),
                ('cod_sicore', models.IntegerField()),
                ('empresue', models.CharField(max_length=2)),
                ('activo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hliquidac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.IntegerField()),
                ('concepto', models.CharField(max_length=10)),
                ('monto', models.FloatField()),
                ('nro_liq', models.BigIntegerField()),
                ('mes', models.IntegerField()),
            ],
        ),
    ]
