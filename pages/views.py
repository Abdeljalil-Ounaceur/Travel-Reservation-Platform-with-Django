from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Categorie, Voyage, Promotion, Reservation, Notification

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

def login_validation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if user.is_staff:
                return HttpResponseRedirect('admindashboard')
            else:
                return HttpResponseRedirect('clientdashboard')
        else:
            # Return an 'invalid login' error message.
            return render(request, "pages/LoginSingUp.html", {"error": "Invalid login"})
    else:
        return render(request, "pages/LoginSingUp.html")

def signup_validation(request):
    if request.method == 'POST':
        first_name = request.POST.get('prenom')
        last_name = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Create user
        user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
        )
        # Log in the user
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect('clientdashboard')
    else:
        return render(request, "pages/LoginSingUp.html")

# Create your views here.
