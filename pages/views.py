import datetime
import io
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password   
from .models import CustomUser, Categorie, Offre, Promotion, Reservation, Notification, Message
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template.loader import get_template
from django.template import Context
import secrets
import stripe
from django.template import Context



stripe.api_key = "sk_test_51OaJ54AyNfWQ41o0yvnqrz8RysqN2LUd4ZZLRV7XPj0FEvzhjjVjUWaA39GcjegB764bjTTypYBetN22Ve5kL6v600q9DlvDzL"

def payment_page(request) :
    if request.method == 'POST':
        stripe.Customer.create(
            name = request.POST.get('name'),
            email = request.POST.get('email')
        )
        stripe.Charge.create(
        amount=1585,
        currency="usd",
        source="tok_visa",
        )
    return render(request,'pages/payment.html')

def checkout_page(request) :
    return render(request,'pages/Checkout.html')

def accuile_page(request) :
    categories = Categorie.objects.all().reverse()[:3]
    offers = Offre.objects.all().reverse()[:3]
    return render(request,'pages/index.html', {'categories':categories, 'offers':offers})

def login_SingUp_Page(request) :
    return render(request,'pages/LoginSingUp.html')

def contact_us_page(request) :
    return render(request,'pages/ContactUs.html')
def about_us_page(request) :
    return render(request,'pages/AboutUs.html')
def package_page(request) :
    categories = Categorie.objects.all()
    return render(request,'pages/Package.html', {'categories': categories})
def offers_page(request) :
    print(request.GET)
    filters = {
        'minPrice' : int(request.GET.get('minPrice')) if request.GET.get('minPrice') else None,
        'maxPrice' : int(request.GET.get('maxPrice')) if request.GET.get('maxPrice') else None,
        'minDuration' : int(request.GET.get('minDuration')) if request.GET.get('minDuration') else None,
        'maxDuration' : int(request.GET.get('maxDuration')) if request.GET.get('maxDuration') else None,
        'sort': request.GET.get('sort'),
        'categorie':int(request.GET.get('categorie')) if request.GET.get('categorie') else None
    }
    offers_unfiltered = Offre.objects.all()
    offers = []
    for offer in offers_unfiltered:
        days = (offer.date_fin - offer.date_debut).days
        if filters['minPrice'] and offer.prix < filters['minPrice'] \
        or filters['maxPrice'] and offer.prix > filters['maxPrice'] \
        or filters['minDuration'] and  days < filters['minDuration'] \
        or filters['maxDuration'] and days > filters['maxDuration'] \
        or filters['categorie'] and ( not offer.categorie or offer.categorie.id != filters['categorie']) :
            continue
        offers.append(offer)
    
    offers.sort(key=lambda offer:offer.date_debut)
    
    categories = Categorie.objects.all()
    return render(request,'pages/Offers.html', {'offers': offers, 'categories':categories, 'filters':filters})

def client_message(request) :
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Message.objects.create(name=name, email=email, message=message)
        messages.info(request,"Message sent successfully")
        return render(request,'pages/ContactUs.html')
    messages.info(request,"Message not sent")
    return render(request,'pages/ContactUs.html')

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
            messages.info(request,"Check email or password")
            return render(request,'pages/LoginSingUp.html')
    else:
        return render(request, "pages/LoginSingUp.html")

def signup_validation(request):
    if request.method == 'POST':
        first_name = request.POST.get('prenom')
        last_name = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if CustomUser.objects.filter(email=email).exists() :
                messages.info(request,"Email already exists")
                return render(request,'pages/LoginSingUp.html')
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
    

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        user = request.user
        if user.check_password(old_password):
            print('correct password')
            user.set_password(new_password)
            user.save()
            logout(request)
            return redirect('login_SingUp_Page')

    if(user.is_staff):
        return redirect('admindashboard/settings')
    else:
        return redirect('clientdashboard/settings')

#update personal information

def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        if user.is_staff:
            return HttpResponseRedirect('admindashboard')
        else:
            return HttpResponseRedirect('clientdashboard')
    else:
        return redirect('admindashboard')


#logout_view 
def logout_view(request):
    logout(request)
    return redirect('accuilepage')

# Create your views here.
#validation email :

def email_validation(request):
    if request.method == 'POST':
        first_name = request.POST.get('prenom')
        last_name = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return render(request, 'pages/LoginSingUp.html')

        verification_code = secrets.token_hex(4)
        subject = "Verification Code"
        from_email = "med@mail.com"  # Replace with your email
        to_email = [email]

        html_message = render_to_string('test.html', {'verification_code': verification_code})

        email_message = EmailMessage(
            subject=subject,
            body=html_message,  # HTML content goes here
            from_email=from_email,
            to=to_email,
        )
        email_message.content_subtype = "html"
        email_message.send()
        request.session['first_name'] = first_name
        request.session['last_name'] = last_name
        request.session['password'] = password
        request.session['email'] = email
        request.session['verification_code'] = verification_code
        return render(request, "pages/SaisirVerificationCode.html")

    # Handle other HTTP methods if needed
    return render(request, "pages/LoginSingUp.html")

def get_verificaioncode(request) :  
    VeriCode = request.POST.get('VeriCode')
    verification_code = request.session.get('verification_code', '')
    first_name = request.session.get('first_name', '')
    last_name = request.session.get('last_name', '')
    email = request.session.get('email', '')
    password = request.session.get('password', '')
    if VeriCode == verification_code :
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
        messages.info(request, "Invalide Code")
        return render(request, "pages/SaisirVerificationCode.html")   
# test emails : 

def simple_mail(request):
    subject = "Verification Code"
    from_email = "med@mail.com"
    to_email = ["jalilo@mail.com"]

    # Generate a random verification code
    verification_code = secrets.token_hex(4)  # You can adjust the length as needed

    # Render the HTML content from the "verification_code.html" template
    html_message = render_to_string('test.html', {'verification_code': verification_code})

    # Create an EmailMessage instance
    email_message = EmailMessage(
        subject=subject,
        body=html_message,  # HTML content goes here
        from_email=from_email,
        to=to_email,
    )

    # Specify the content type as "text/html"
    email_message.content_subtype = "html"

    # Send the email
    email_message.send()

    return HttpResponse("Verification email sent successfully")

def reserver_offre(request,offer_id):
    offer = get_object_or_404(Offre, id=offer_id)
    reservation = Reservation.objects.create(
            offre = offer,
            utilisateur = request.user,
            date = datetime.datetime.now()
        )
    reservation.save()
    return redirect("clientdashboard")
