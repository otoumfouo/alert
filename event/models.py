from datetime import datetime

from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.
class Region(models.Model):
    nom = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nom


class Departement(models.Model):
    nom = models.CharField(max_length=90)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nom


class Commune(models.Model):
    nom = models.CharField(max_length=90)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nom


class Camera(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom de la camera")
    adresse_ip = models.CharField(max_length=70)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = ("Camera")
        verbose_name_plural = ("Cameras")

    def __str__(self):
        return self.nom


class Categorie_evmt(models.Model):
    nom = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nom


class Evenement(models.Model):
    nom = models.CharField(max_length=90)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lieu = models.CharField(max_length=70)
    categorie_event = models.ForeignKey(Categorie_evmt, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nom


class Type_degats(models.Model):
    libelle = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.libelle

class Organisateurs(models.Model):
    nom = models.CharField(max_length=70)
    telephone = models.IntegerField()
    fonction = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nom


class Intervenants(models.Model):
    nom = models.CharField(max_length=70)
    telephone = models.CharField(max_length=70)
    #fonction = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nom


class Statu(models.Model):
    libelle = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.libelle


class Type_alert(models.Model):
    libelle = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.libelle

class Capteur_alert(models.Model):
    libelle = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.libelle



class Alert(models.Model):
    lieu = models.CharField(max_length=30, verbose_name=("Adresse géographique"))
    datedebut = models.DateTimeField(verbose_name=(" Date de Debut Incident"))
    datefin = models.DateTimeField(null=True, blank=True, verbose_name=(" Date de Fin Incident"))
    description = models.CharField(max_length=255,verbose_name=("description Suscinte"))
    commentaire = models.TextField(null=True, blank=True,verbose_name=("description Complete"))
    created = models.DateTimeField(auto_now_add=True)
    intervenant = models.ForeignKey(Intervenants, on_delete=models.CASCADE,
                                    related_name="alert_interv", null=True, blank=True)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE,related_name="event_alert", null=True, blank=True)
    type = models.ForeignKey(Type_alert, on_delete=models.CASCADE,related_name="type_alert", verbose_name=("Type d'Incident"))
    source_information = models.ForeignKey(Capteur_alert, on_delete=models.CASCADE,related_name="capteur_alert", verbose_name=("Source d'Information Incident"))
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE,related_name="commune_alert")
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE,related_name="event_alert", null=True, blank=True)
    #statu = models.ForeignKey(Statu, on_delete=models.CASCADE,related_name="etat_alert")
    image = models.FileField(verbose_name=("fichier"), upload_to="static/media/alert/",
                             max_length=300, null=True, blank=True)
    organisateur = models.ForeignKey(Organisateurs, on_delete=models.CASCADE,
                                    related_name="alert_org", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.datedebut = self.datedebut
        super(Alert, self).save(*args, **kwargs)

    def __str__(self):
        return self.lieu


class Degats(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name="degat_alert")
    type_degat = models.ForeignKey(Type_degats, on_delete=models.CASCADE, related_name="type_degat_alert")
    created_at = models.DateTimeField(auto_now_add=True)
    nbre = models.IntegerField()
    #observation = models.TextField()

