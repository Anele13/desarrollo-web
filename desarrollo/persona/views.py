#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import FormularioUsuario
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, 'persona/agente.html')

def salir(request):
    logout(request)
    return redirect('login')

def login_usuario(request):
    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('cuil')
            contraseña = form.cleaned_data.get('contraseña')
            usuario= form.obtener_o_crear(username, contraseña)
            login(request, usuario)
            return redirect('mostrar_agente')
    else:
        form = FormularioUsuario()
    return render(request, 'registration/login.html', {'form': form})


def mostrar_agente(request):
    if request.method=='POST':
        null
    return render(request, 'persona/agente.html')

def mostrar_administrador(request):
    return reder(request, 'persona/adminsitrador.html')
