from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogue, name='home'), 
    path('hotel/<int:hotel_id>/', views.voir_hotel, name='voir_hotel'),
    path('reservation/<int:chambre_id>/', views.creer_reservation, name='creer_reservation'),
    path('chatbot/', views.chatbot, name='chatbot'),
    
    path('mes-reservations/', views.mes_reservations, name='mes_reservations'),
]