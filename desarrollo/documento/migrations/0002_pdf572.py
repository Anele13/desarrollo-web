# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf572',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuil', models.CharField(max_length=13)),
                ('periodo', models.CharField(max_length=8)),
                ('presentacion', models.IntegerField()),
                ('docfile', models.FileField(upload_to='formulario_f572/')),
            ],
        ),
    ]
