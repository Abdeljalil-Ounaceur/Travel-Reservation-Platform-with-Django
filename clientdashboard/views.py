from django.shortcuts import render
from django.http import HttpResponse

def accuile_page(request) :
    return render(request,'clientdashboard/client.html')

def settings_page(request) :
    return render(request,'clientdashboard/settings.html')

def contactus_page(request) :
    return render(request,'clientdashboard/contactus.html')