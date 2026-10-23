from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Opcion

def lista_votaciones(request):
    opciones = Opcion.objects.all()
    return render(request, 'votaciones/index.html', {'opciones': opciones})

@login_required
def registrar_voto(request, opcion_id):
    if request.method == 'POST':
        opcion = get_object_or_404(Opcion, id=opcion_id)
        opcion.votos = (opcion.votos or 0) + 1
        opcion.save()
    return redirect('lista_votaciones')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_votaciones')
    else:
        form = UserCreationForm()
    return render(request, 'votaciones/registro.html', {'form': form})