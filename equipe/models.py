from django.db import models
class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero = models.IntegerField()
    poste= models.CharField(max_length=50)


def __str__(self):
        return f"{self.prenom} {self.nom} {self.numero}"

class Match(models.Model):
    adversaire = models.CharField(max_length=100)
    date = models.DateField()
    lieu = models.CharField(max_length=100)
    score_equipe = models.PositiveIntegerField(null=True, blank=True)
    score_adversaire = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.adversaire} - {self.date.strftime('%d/%m/%Y')}"





# Create your models here.
