# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0002_pdf572'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf572',
            name='cuil',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pdf572',
            name='periodo',
            field=models.IntegerField(),
        ),
    ]
