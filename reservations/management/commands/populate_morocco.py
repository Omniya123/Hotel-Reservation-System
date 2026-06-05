from django.core.management.base import BaseCommand
from reservations.models import Hotel, TypeChambre, Chambre
import random

class Command(BaseCommand):
    help = 'Populates the database with Moroccan hotels, room types, and rooms'

    def handle(self, *args, **kwargs):
        self.stdout.write("Configuring Room Types...")
        
        
        types_config = [
            {"libelle": "Chambre Standard", "capacite": 2},
            {"libelle": "Chambre Executive", "capacite": 3},
            {"libelle": "Suite Royale Luxe", "capacite": 4},
        ]
        
        types_enregistres = []
        for tc in types_config:
            type_ch, _ = TypeChambre.objects.get_or_create(
                libelle=tc["libelle"],
                defaults={"capacite_personnes": tc["capacite"]}
            )
            types_enregistres.append(type_ch)

        
        moroccan_data = [
            {"nom": "Hotel Atlantique Safi", "ville": "Safi", "adresse": "Boulevard Mohamed V", "equipements": "Vue sur mer, WiFi, Restaurant"},
            {"nom": "Riad Dar Plasma", "ville": "Marrakech", "adresse": "Médina, Jemaa el-Fna", "equipements": "Piscine, Spa, Climatisation, Petit-déjeuner"},
            {"nom": "Tour Hassan Palace", "ville": "Rabat", "adresse": "Quartier Hassan", "equipements": "WiFi, Piscine, Salle de sport, Business Center"},
            {"nom": "Casablanca Marina Bay", "ville": "Casablanca", "adresse": "Boulevard de la Corniche", "equipements": "WiFi, Gym, Parking gratuit, Bar"},
            {"nom": "El Minzah Hotel", "ville": "Tanger", "adresse": "Rue de la Liberté", "equipements": "Piscine, WiFi, Restaurant traditionnel"},
            {"nom": "Agadir Beach Club", "ville": "Agadir", "adresse": "Secteur Touristique", "equipements": "Accès Plage, Piscine, All Inclusive"},
            {"nom": "Fes Marriott Jnan Palace", "ville": "Fes", "adresse": "Avenue Ahmed Chaouki", "equipements": "Spa, Grand Jardin, WiFi, Clim"},
            {"nom": "Hotel Transatlantique", "ville": "Meknes", "adresse": "Rue El Meriniyne", "equipements": "Piscine, WiFi, Parking"},
            {"nom": "Atlas Terminus Oriental", "ville": "Oujda", "adresse": "Boulevard Abdellah Chefchaouni", "equipements": "WiFi, Restaurant, Piscine"},
            {"nom": "Hotel Kenzi Solazur", "ville": "Tetouan", "adresse": "Route de Ceuta", "equipements": "WiFi, Climatisation, Proche Plage"},
        ]

        self.stdout.write("Populating Hotels and distributing rooms...")
        
        for item in moroccan_data:
            # Create or fetch the hotel
            hotel, created = Hotel.objects.get_or_create(
                nom=item["nom"],
                defaults={
                    "ville": item["ville"],
                    "adresse": item["adresse"],
                    "equipements": item["equipements"],
                    "description": f"Bienvenue au magnifique {item['nom']} situé au cœur de la ville de {item['ville']}."
                }
            )

            
            if not Chambre.objects.filter(hotel=hotel).exists():
                for i, t_chambre in enumerate(types_enregistres):
                    numero_base = random.randint(100, 500) + i
                    prix_base = 400 + (i * 250) 
                    
                    Chambre.objects.create(
                        numero_chambre=str(numero_base),
                        hotel=hotel,
                        type_chambre=t_chambre,
                        prix_base_nuit=prix_base,
                        est_active=True
                    )
                self.stdout.write(self.style.SUCCESS(f"Generated 3 active rooms for {hotel.nom} ({hotel.ville})"))

        self.stdout.write(self.style.SUCCESS("All Moroccan systems completely loaded with hotels and rooms!"))