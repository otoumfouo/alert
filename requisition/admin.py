from django.contrib import admin
from requisition.models import *
# Register your models here.
@admin.register(Requerant)
class RequerantAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'contacts','created_at',)
    list_filter = ('libelle', 'created_at',)
    search_fields = ('libelle', 'created_at',)
