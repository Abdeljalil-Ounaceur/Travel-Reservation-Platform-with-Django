from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from pages.models import Reservation

def accuile_page(request) :
    reserations = Reservation.objects.filter(utilisateur=request.user).reverse()
    for reservation in reserations :
        reservation.status = reservation.offre.date_debut > reservation.date

    return render(request,'clientdashboard/client.html',{'reservations':reserations})

def settings_page(request) :
    return render(request,'clientdashboard/settings.html')

def contactus_page(request) :
    return render(request,'clientdashboard/contactus.html')