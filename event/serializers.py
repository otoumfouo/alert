from rest_framework import serializers
from .models import *

class Capteur_alertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Capteur_alert
        fields  = ['id', 'libelle']
class Type_alertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Type_alert
        fields = ['id', 'libelle']
class communeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Commune
        fields = ['id', 'nom']




class AlbumSerializer(serializers.ModelSerializer):
    capteur = Capteur_alertSerializer()
    type = Type_alertSerializer()
    commune = communeSerializer()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Alert
        fields = ['capteur_libelle', 'datedebut', 'type_libelle', 'commune_nom', 'description']
