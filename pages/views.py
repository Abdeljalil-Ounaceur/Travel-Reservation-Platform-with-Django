from django.shortcuts import render
from django.http import HttpResponse

def accuile_page(request) :
    return render(request,'pages/index.html')

def login_SingUp_Page(request) :
    return render(request,'pages/LoginSingUp.html')

def contact_us_page(request) :
    return render(request,'pages/ContactUs.html')
def about_us_page(request) :
    return render(request,'pages/AboutUs.html')
def package_page(request) :
    return render(request,'pages/Package.html')
def offers_page(request) :
    return render(request,'pages/Offers.html')


# Create your views here.
