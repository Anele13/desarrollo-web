# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
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
            name='LiqFin',
            fields=[
                ('descrip', models.CharField(max_length=100, null=True)),
                ('periodo', models.IntegerField(blank=True, null=True)),
                ('ecuit', models.CharField(blank=True, max_length=100, null=True)),
                ('documento', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nya', models.CharField(max_length=100)),
                ('empliq', models.CharField(blank=True, max_length=100, null=True)),
                ('cuit', models.CharField(blank=True, max_length=100, null=True)),
                ('wcalle', models.CharField(blank=True, max_length=100, null=True)),
                ('wnro', models.CharField(blank=True, max_length=100, null=True)),
                ('wpiso', models.CharField(blank=True, max_length=100, null=True)),
                ('wdpto', models.CharField(blank=True, max_length=100, null=True)),
                ('wlocalidad', models.CharField(blank=True, max_length=100, null=True)),
                ('wprovincia', models.CharField(blank=True, max_length=100, null=True)),
                ('wcp', models.CharField(blank=True, max_length=100, null=True)),
                ('r01_00', models.CharField(blank=True, max_length=100, null=True)),
                ('r01a00', models.CharField(blank=True, max_length=100, null=True)),
                ('r01b00', models.CharField(blank=True, max_length=100, null=True)),
                ('r01c00', models.CharField(blank=True, max_length=100, null=True)),
                ('r01d00', models.CharField(blank=True, max_length=100, null=True)),
                ('r01z00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02_00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02a00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02b00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02c00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02d00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02e00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02f00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02g00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02h00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02i00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02j00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02k00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02l00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02m00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02n00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02o00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02p00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02q00', models.CharField(blank=True, max_length=100, null=True)),
                ('r02z00', models.CharField(blank=True, max_length=100, null=True)),
                ('r03_00', models.CharField(blank=True, max_length=100, null=True)),
                ('r03a00', models.CharField(blank=True, max_length=100, null=True)),
                ('r03b00', models.CharField(blank=True, max_length=100, null=True)),
                ('r03c00', models.CharField(blank=True, max_length=100, null=True)),
                ('r03d00', models.CharField(blank=True, max_length=100, null=True)),
                ('r03e00', models.CharField(blank=True, max_length=100, null=True)),
                ('r03z00', models.CharField(blank=True, max_length=100, null=True)),
                ('r04_00', models.CharField(blank=True, max_length=100, null=True)),
                ('r04a00', models.CharField(blank=True, max_length=100, null=True)),
                ('r04b00', models.CharField(blank=True, max_length=100, null=True)),
                ('r04c00', models.CharField(blank=True, max_length=100, null=True)),
                ('r04z00', models.CharField(blank=True, max_length=100, null=True)),
                ('saldo', models.CharField(blank=True, max_length=100, null=True)),
                ('saldoafip', models.CharField(blank=True, max_length=100, null=True)),
                ('saldoben', models.CharField(blank=True, max_length=100, null=True)),
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
