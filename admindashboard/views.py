from django.shortcuts import render
from django.http import HttpResponse

def accuile_page(request) :
    return render(request,'admindashboard/index.html')

def category_page(request) :
    return render(request,'admindashboard/category.html')

def client_page(request) :
    return render(request,'admindashboard/client.html')

def contactus_page(request) :
    return render(request,'admindashboard/contactus.html')

def newcategory_page(request) :
    return render(request,'admindashboard/newcategory.html')

def newoffer_page(request) :
    return render(request,'admindashboard/newoffer.html')

def offers_page(request) :
    return render(request,'admindashboard/offers.html')

def settings_page(request) :
    return render(request,'admindashboard/settings.html')


# Create your views here.
