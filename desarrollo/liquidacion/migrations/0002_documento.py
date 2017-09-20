# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquidacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('docfile', models.FileField(upload_to='csv/%Y/%m/%d')),
            ],
        ),
    ]
