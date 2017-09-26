# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 12:14
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('documento', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nya', models.CharField(max_length=30)),
                ('empliq', models.CharField(blank=True, max_length=10, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=2, null=True)),
                ('cuil', models.CharField(blank=True, max_length=15, null=True)),
                ('f572', models.IntegerField(blank=True, null=True)),
                ('fechaf572', models.DateField(blank=True, null=True)),
                ('observ', models.CharField(blank=True, max_length=255, null=True)),
                ('fechapres', models.DateField(blank=True, null=True)),
                ('nropres', models.IntegerField(blank=True, null=True)),
                ('famok', models.IntegerField(blank=True, null=True)),
                ('excep', models.IntegerField(blank=True, null=True)),
                ('web', models.IntegerField(blank=True, null=True)),
                ('fechaweb', models.DateField(blank=True, null=True)),
                ('wcuit', models.CharField(blank=True, max_length=15, null=True)),
                ('wtipodoc', models.CharField(blank=True, choices=[('80', 'Cuit'), ('86', 'Cuil')], max_length=5, null=True)),
                ('wapellido', models.CharField(blank=True, max_length=50, null=True)),
                ('wnombre', models.CharField(blank=True, max_length=50, null=True)),
                ('wdireccion', models.CharField(blank=True, max_length=50, null=True)),
                ('wprovincia', models.CharField(blank=True, max_length=50, null=True)),
                ('wcp', models.CharField(blank=True, max_length=30, null=True)),
                ('wlocalidad', models.CharField(blank=True, max_length=60, null=True)),
                ('wcalle', models.CharField(blank=True, max_length=40, null=True)),
                ('wnro', models.CharField(blank=True, max_length=10, null=True)),
                ('wpiso', models.CharField(blank=True, max_length=10, null=True)),
                ('wdpto', models.CharField(blank=True, max_length=10, null=True)),
                ('wcuitreten', models.CharField(blank=True, max_length=20, null=True)),
                ('wdescreten', models.CharField(blank=True, max_length=200, null=True)),
                ('periodo', models.IntegerField(blank=True, null=True)),
                ('revisado', models.CharField(blank=True, max_length=10, null=True)),
                ('administrador', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.Administrador')),
                ('agente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.Agente')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
