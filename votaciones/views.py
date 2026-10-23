from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Opcion, Votacion

def lista_votaciones(request):
    # Trae todas las opciones registradas para mostrarlas en la pagina principal
    opciones = Opcion.objects.all()
    return render(request, 'votaciones/index.html', {'opciones': opciones})

@login_required
def registrar_voto(request, opcion_id):
    if request.method == 'POST':
        opcion = get_object_or_404(Opcion, id=opcion_id)
        opcion.votos += 1
        opcion.save()
        return redirect('lista_votaciones')
    return redirect('lista_votaciones')