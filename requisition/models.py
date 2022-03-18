from django.db import models
from event.models import *


# Create your models here.
class Requerant(models.Model):
    libelle = models.CharField(max_length=90)
    contacts = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.libelle


class Requistion(models.Model):
    num_requistion = models.CharField(max_length=90)
    objet = models.CharField(max_length=90)
    dpll = models.FileField(verbose_name=("fichier de la requistion"), upload_to="static/media/requisition/",
                            max_length=300)
    requerant = models.ForeignKey(Requerant, on_delete=models.CASCADE, related_name="requerants")
    created_at = models.DateTimeField(auto_now_add=True)
    date_demande = models.DateField( null=True, blank=True)
    commentaire = models.TextField(null=True, blank=True, verbose_name=("Contexte de la demande"))
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.num_requistion


class Rapport(models.Model):
    introduction = models.CharField(max_length=90)
    conlusion = models.CharField(max_length=90)
    requistion = models.ForeignKey(Requistion, on_delete=models.CASCADE, related_name="requerant_requ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.introduction


class RapportDetail(models.Model):
    mise_en_cause = models.CharField(max_length=90)
    observation = models.CharField(max_length=90)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name="camera_requ")
    rapport = models.ForeignKey(Rapport, on_delete=models.CASCADE, related_name="rapport_requ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.observation

class RapportImages(models.Model):
    rapport = models.ForeignKey(Rapport, on_delete=models.CASCADE, related_name="rapport_requ_simage")
    image = models.FileField(verbose_name=("fichier"), upload_to="static/media/requisition/",
                            max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.image
