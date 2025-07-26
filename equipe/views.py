from django.shortcuts import render
from .models import Joueur

def liste_joueurs(request):
    joueurs = Joueur.objects.all()
    return render(request, 'equipe/liste_joueurs.html', {'joueurs': joueurs})

from .models import Match

def calendrier(request):
    matchs = Match.objects.all().order_by('date')
    return render(request, 'equipe/calendrier.html', {'matchs': matchs})
from django.urls import path
from . import views

urlpatterns = [
    path('joueurs/', views.liste_joueurs, name='liste_joueurs'),
    path('calendrier/', views.calendrier, name='calendrier'),
]
