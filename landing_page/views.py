from django.shortcuts import render
from .listas_bebidas import bebidas

def landing_page(request):
    return render(request, 'landing_page/landing_page.html', {'bebidas': bebidas})

# views.py
from django.shortcuts import render
from .listas_bebidas import bebidas
from .listas_consolas import consolas

def landing_page(request):
    context = {
        'bebidas': bebidas,
        'consolas': consolas
    }
    return render(request, 'landing_page/landing_page.html', context)

