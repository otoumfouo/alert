from django.contrib import admin
from .models import *


# Register your models here.

class DepartementInline(admin.TabularInline):
    model = Departement


class CommuneInline(admin.TabularInline):
    model = Commune


class DegatInline(admin.TabularInline):
    model = Degats





@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'created_at',)
    list_filter = ('nom', 'created_at',)
    search_fields = ('nom', 'created_at',)
    inlines = [DepartementInline]


@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    inlines = [CommuneInline]
    list_display = ('nom', 'region', 'created_at',)
    list_filter = ('nom', 'region', 'created_at',)
    search_fields = ('nom', 'created_at', 'region',)


@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'departement', 'created_at',)
    list_filter = ('nom', 'departement', 'created_at',)
    search_fields = ('nom', 'created_at', 'departement',)


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse_ip', 'commune', 'created_at',)
    list_filter = ('nom', 'adresse_ip', 'commune', 'created_at',)
    search_fields = ('nom', 'adresse_ip', 'commune', 'created_at',)


@admin.register(Categorie_evmt)
class Categorie_evmtAdmin(admin.ModelAdmin):
    list_display = ('nom', 'created_at',)
    list_filter = ('nom', 'created_at',)
    search_fields = ('nom', 'created_at',)


@admin.register(Type_degats)
class Type_degatsAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'created_at',)
    list_filter = ('libelle', 'created_at',)
    search_fields = ('libelle', 'created_at',)


@admin.register(Type_alert)
class Type_alertAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'created_at',)
    list_filter = ('libelle', 'created_at',)
    search_fields = ('libelle', 'created_at',)


@admin.register(Capteur_alert)
class Capteur_alertAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'created_at',)
    list_filter = ('libelle', 'created_at',)
    search_fields = ('libelle', 'created_at',)


@admin.register(Intervenants)
class IntervenantsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'created_at',)
    list_filter = ('nom', 'telephone', 'created_at',)
    search_fields = ('nom', 'telephone', 'created_at',)


@admin.register(Statu)
class StatuAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'created_at',)
    list_filter = ('libelle', 'created_at',)
    search_fields = ('libelle', 'created_at',)


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('evenement', 'intervenant', 'lieu', 'datedebut', 'datefin', 'created',)
    list_filter = ('evenement', 'intervenant',)
    search_fields = ('evenement', 'intervenant',)
    inlines = [ DegatInline]


@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'lieu', 'date_debut', 'date_fin', 'created_at',)
    list_filter = ('nom', 'lieu')
    search_fields = ('nom', 'lieu')
    # inlines = [Fichiers_alertInline,DegatInline]
