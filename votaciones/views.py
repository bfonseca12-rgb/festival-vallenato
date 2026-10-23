from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Opcion

def lista_votaciones(request):
    # Consulta directa y liviana para evitar bloqueos
    opciones = Opcion.objects.all()
    return render(request, 'votaciones/index.html', {'opciones': opciones})

@login_required
def registrar_voto(request, opcion_id):
    if request.method == 'POST':
        opcion = get_object_or_404(Opcion, id=opcion_id)
        opcion.votos = (opcion.votos or 0) + 1
        opcion.save()
    return redirect('lista_votaciones')