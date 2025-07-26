from django.urls import path
from . import views

urlpatterns = [
    path('joueurs/', views.liste_joueurs, name='liste_joueurs'),
    path('calendrier/', views.calendrier, name='calendrier'),
]
