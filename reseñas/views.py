# reseñas/views.py
from django.shortcuts import render, redirect
from .models import Reseña
from .forms import ReseñaForm

def reseñas(request):
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reseñas')
    else:
        form = ReseñaForm()

    reseñas_existentes = Reseña.objects.all()
    return render(request, 'reseñas/reseñas.html', {'form': form, 'reseñas': reseñas_existentes})
