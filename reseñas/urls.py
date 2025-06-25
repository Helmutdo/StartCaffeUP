# reseñas/urls.py
from django.urls import path
from .views import reseñas

urlpatterns = [
    path('', reseñas, name='reseñas'),
]
