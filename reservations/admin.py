from django.contrib import admin
from .models import Hotel, TypeChambre, Chambre, Reservation, Disponibilite, Tarif, Avis

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'adresse', 'latitude', 'longitude')
    list_filter = ('ville',)
    search_fields = ('nom', 'ville')

@admin.register(TypeChambre)
class TypeChambreAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle') 

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
    list_display = ('numero_chambre', 'hotel', 'type_chambre', 'prix_base_nuit') 
    list_filter = ('hotel', 'type_chambre') 
    search_fields = ('numero_chambre',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'chambre', 'nom_client', 'date_arrivee', 'date_depart', 'statut_paiement') 
    list_filter = ('statut_paiement', 'date_arrivee')
    search_fields = ('nom_client',)

@admin.register(Disponibilite)
class DisponibiliteAdmin(admin.ModelAdmin):
    list_display = ('chambre', 'date', 'est_disponible')
    list_filter = ('est_disponible', 'date')

@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    list_display = ('chambre', 'date', 'prix_calcule')

@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'auteur', 'note')
    list_filter = ('note',)