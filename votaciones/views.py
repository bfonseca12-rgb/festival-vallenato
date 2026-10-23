from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Edicion, Votacion, Opcion

def lista_votaciones(request):
    ediciones = Edicion.objects.all()
    votaciones_activas = Votacion.objects.filter(activa=True)
    
    # Obtenemos las votaciones donde la sesión o el usuario ya votó
    votadas = request.session.get('votaciones_realizadas', [])
    
    context = {
        'ediciones': ediciones,
        'votaciones': votaciones_activas,
        'votadas': votadas,
    }
    return render(request, 'votaciones/index.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente tras registrarse
            return redirect('lista_votaciones')
    else:
        form = UserCreationForm()
    return render(request, 'votaciones/registro.html', {'form': form})

@login_required
def registrar_voto(request, opcion_id):
    if request.method == 'POST':
        opcion = get_object_or_404(Opcion, id=opcion_id)
        votacion_id = opcion.votacion.id
        
        votaciones_realizadas = request.session.get('votaciones_realizadas', [])
        
        if votacion_id not in votaciones_realizadas:
            opcion.votos += 1
            opcion.save()
            
            votaciones_realizadas.append(votacion_id)
            request.session['votaciones_realizadas'] = votaciones_realizadas
            
    return redirect('lista_votaciones')