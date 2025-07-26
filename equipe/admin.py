from django.contrib import admin
from .models import Joueur, Match  # <-- importe les deux modèles

admin.site.register(Joueur)        # <-- garde UNE SEULE fois cette ligne
admin.site.register(Match)




# Register your models here.
