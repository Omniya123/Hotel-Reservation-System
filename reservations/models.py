from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Hotel(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=50)
    adresse = models.TextField()
    equipements = models.TextField(help_text="Séparés par des virgules")
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    
    photo = ProcessedImageField(
        upload_to='hotels/',
        processors=[ResizeToFill(800, 450)],
        format='JPEG',
        options={'quality': 80},
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.nom} ({self.ville})"

class TypeChambre(models.Model):
    libelle = models.CharField(max_length=50) # Standard, Suite, etc.

    def __str__(self):
        return self.libelle

class Chambre(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='chambres')
    type_chambre = models.ForeignKey(TypeChambre, on_delete=models.CASCADE)
    numero_chambre = models.CharField(max_length=10)
    prix_base_nuit = models.FloatField()

    def __str__(self):
        return f"Chambre {self.numero_chambre} - {self.hotel.nom}"

class Reservation(models.Model):
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    nom_client = models.CharField(max_length=100)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    statut_paiement = models.CharField(max_length=50, default="En attente")
    stripe_intent_id = models.CharField(max_length=255, blank=True, null=True) # 💳 Suivi Stripe

    def __str__(self):
        return f"Réservation de {self.nom_client} ({self.date_arrivee})"

class Disponibilite(models.Model):
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date = models.DateField()
    est_disponible = models.BooleanField(default=True)

class Tarif(models.Model):
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date = models.DateField()
    prix_calcule = models.FloatField()

class Avis(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100)
    commentaire = models.TextField()
    note = models.IntegerField()