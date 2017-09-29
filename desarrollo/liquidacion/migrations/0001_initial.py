# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabliq',
            fields=[
                ('liqnro', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('indice', models.IntegerField()),
                ('descrip', models.CharField(max_length=50)),
                ('cierre', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('descrip', models.CharField(max_length=150, null=True)),
                ('prorratea', models.FloatField(null=True)),
                ('orden', models.IntegerField(null=True)),
                ('grupo', models.IntegerField(null=True)),
                ('modulo', models.IntegerField(null=True)),
                ('topepro', models.FloatField(null=True)),
                ('signo', models.CharField(max_length=150, null=True)),
                ('concepto', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('grupotope', models.CharField(max_length=10, null=True)),
                ('muestraliq', models.IntegerField(null=True)),
                ('anexas', models.IntegerField(null=True)),
                ('vista', models.IntegerField(null=True)),
                ('titulo', models.IntegerField(null=True)),
                ('of649', models.CharField(max_length=150, null=True)),
                ('ordenliq', models.CharField(max_length=150, null=True)),
                ('fliqfin', models.CharField(max_length=150, null=True)),
                ('grupolf', models.IntegerField(null=True)),
                ('ldescrip', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('codemp', models.IntegerField(primary_key=True, serialize=False)),
                ('saf', models.IntegerField(null=True)),
                ('descrip', models.CharField(max_length=50, null=True)),
                ('claveseg', models.CharField(max_length=50, null=True)),
                ('codtipo', models.IntegerField(null=True)),
                ('excep', models.IntegerField(null=True)),
                ('safcentral', models.IntegerField(null=True)),
                ('cuit', models.CharField(max_length=13, null=True)),
                ('calle', models.CharField(max_length=30, null=True)),
                ('nro', models.IntegerField(null=True)),
                ('codsicore', models.IntegerField(null=True)),
                ('empresue', models.CharField(max_length=2, null=True)),
                ('activo', models.IntegerField(null=True)),
                ('administrador_Responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.Administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Hliquidac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('monto', models.FloatField(null=True)),
                ('concepto', models.ForeignKey(db_column='concepto', on_delete=django.db.models.deletion.CASCADE, to='liquidacion.Concepto')),
                ('documento', models.ForeignKey(db_column='documento', on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PersonaEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('totalhab', models.FloatField(null=True)),
                ('codemp', models.ForeignKey(db_column='codemp', on_delete=django.db.models.deletion.CASCADE, to='liquidacion.Empresa')),
                ('documento', models.ForeignKey(db_column='documento', on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
            ],
        ),
        migrations.AddField(
            model_name='hliquidac',
            name='mes',
            field=models.ForeignKey(db_column='mes', null=True, on_delete=django.db.models.deletion.CASCADE, to='liquidacion.Mes'),
        ),
        migrations.AddField(
            model_name='hliquidac',
            name='nroliq',
            field=models.ForeignKey(db_column='nroliq', on_delete=django.db.models.deletion.CASCADE, to='liquidacion.Cabliq'),
        ),
        migrations.AddField(
            model_name='cabliq',
            name='mes',
            field=models.ForeignKey(db_column='mes', on_delete=django.db.models.deletion.CASCADE, to='liquidacion.Mes'),
        ),
    ]
