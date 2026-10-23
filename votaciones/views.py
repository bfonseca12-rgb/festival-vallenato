from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Opcion, Votacion

def lista_votaciones(request):
    # Carga optimizada usando select_related para evitar bloqueos en la base de datos
    votaciones = Votacion.objects.all()
    opciones = Opcion.objects.select_related('votacion').all() if hasattr(Opcion, 'votacion') else Opcion.objects.all()
    
    return render(request, 'votaciones/index.html', {
        'opciones': opciones,
        'votaciones': votaciones,
    })

@login_required
def registrar_voto(request, opcion_id):
    if request.method == 'POST':
        opcion = get_object_or_404(Opcion, id=opcion_id)
        opcion.votos = (opcion.votos or 0) + 1
        opcion.save()
    return redirect('lista_votaciones')