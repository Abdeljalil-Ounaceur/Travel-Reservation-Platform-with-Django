from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from pages.models import Reservation
from pages.decorators import  require_client

@require_client
def accuile_page(request) :
    reserations = Reservation.objects.filter(utilisateur=request.user).reverse()
    for reservation in reserations :
        reservation.status = reservation.offre.date_debut > reservation.date

    return render(request,'clientdashboard/client.html',{'reservations':reserations})

@require_client
def settings_page(request) :
    return render(request,'clientdashboard/settings.html')

@require_client
def contactus_page(request) :
    return render(request,'clientdashboard/contactus.html')