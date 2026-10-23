from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Opcion, Votacion

def lista_votaciones(request):
    # Trae todas las opciones sin importar a qué votación pertenezcan
    opciones = Opcion.objects.all()
    votaciones = Votacion.objects.all()
    
    return render(request, 'votaciones/index.html', {
        'opciones': opciones,
        'votaciones': votaciones,
    })

@login_required
def registrar_voto(request, opcion_id):
    if request.method == 'POST':
        opcion = get_object_or_404(Opcion, id=opcion_id)
        # Sumar voto soportando diferentes nombres de campo
        if hasattr(opcion, 'votos'):
            opcion.votos += 1
        elif hasattr(opcion, 'voto'):
            opcion.voto += 1
        opcion.save()
        return redirect('lista_votaciones')
    return redirect('lista_votaciones')