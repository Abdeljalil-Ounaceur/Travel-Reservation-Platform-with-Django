from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

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

def login_verification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print("user exists")
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('clientdashboard')
        else:
            # Return an 'invalid login' error message.
            print("user not exists")
            return render(request, "pages/LoginSingUp.html", {"error": "Invalid login"})
    else:
        print("not post")
        return render(request, "pages/LoginSingUp.html")


# Create your views here.
