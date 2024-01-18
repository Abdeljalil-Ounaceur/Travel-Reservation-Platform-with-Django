from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from pages.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, redirect
from pages.models import Categorie, Offre, Categorie, Promotion


def accuile_page(request) :
    return render(request,'admindashboard/index.html')

def category_page(request) :
    categories = Categorie.objects.all()
    return render(request,'admindashboard/category.html', {'categories': categories})

def client_page(request):
    clients = CustomUser.objects.filter(is_staff=False).order_by('-id')
    return render(request, 'admindashboard/client.html', {'clients': clients})

def newclient_page(request) :
    return render(request,'admindashboard/newclient.html')

def contactus_page(request) :
    return render(request,'admindashboard/contactus.html')

def newcategory_page(request) :
    return render(request,'admindashboard/newcategory.html')

def newoffer_page(request) :
    categories = Categorie.objects.all()
    promotions = Promotion.objects.all()
    return render(request,'admindashboard/newoffer.html', {'categories': categories, 'promotions': promotions})

def offers_page(request) :
    offers = Offre.objects.all()
    categories = Categorie.objects.all()
    return render(request,'admindashboard/offers.html', {'offers': offers, 'categories': categories})

def settings_page(request) :
    return render(request,'admindashboard/settings.html')


def create_client(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_active = request.POST.get('is_active') == 'on'
        user = CustomUser.objects.create(
            email=email,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name,
            is_staff=False,
            is_active=is_active,
        )
        login(request, user)
        return HttpResponseRedirect('client')
    else:
        return redirect('newclient')

def delete_client(request, client_id):
    client = get_object_or_404(CustomUser, id=client_id)
    client.delete()
    return redirect('client')

def edit_client(request, client_id):
    client = get_object_or_404(CustomUser, id=client_id)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_type = request.POST.get('user_type')
        is_staff = True if user_type == 'admin' else False
        is_active = request.POST.get('is_active') == 'on'
        client.email = email
        client.password = make_password(password)
        client.first_name = first_name
        client.last_name = last_name
        client.is_staff = is_staff
        client.is_active = is_active
        client.save()
        return redirect('client')
    else:
        return redirect('client')


def create_category(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        categorie = Categorie.objects.create(
            nom=nom,
            description=description,
            image=image,
        )
        return HttpResponseRedirect('category')
    else:
        return redirect('newcategory')

def edit_category(request, category_id):
    category = get_object_or_404(Categorie, id=category_id)
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category.nom = nom
        category.description = description
        category.image = image
        category.save()
        return redirect('category')
    else:
        return redirect('category')

def delete_category(request, category_id):
    category = get_object_or_404(Categorie, id=category_id)
    category.delete()
    return redirect('category')


def create_offer(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        image = request.FILES.get('image')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        categorie_id = request.POST.get('categorie')
        promotion_id = request.POST.get('promotion')
        categorie = Categorie.objects.get(id=categorie_id)
        promotion = Promotion.objects.get(id=promotion_id) if promotion_id else None
        offre = Offre.objects.create(
            titre=titre,
            description=description,
            prix=prix,
            image=image,
            date_debut=date_debut,
            date_fin=date_fin,
            categorie=categorie,
            promotion=promotion,
        )
        return HttpResponseRedirect('offers')
    else:
        return redirect('newoffer')

def edit_offer(request, offer_id):
    offre = get_object_or_404(Offre, id=offer_id)
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        image = request.FILES.get('image')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        categorie_id = request.POST.get('categorie')
        promotion_id = request.POST.get('promotion')
        categorie = Categorie.objects.get(id=categorie_id)
        promotion = Promotion.objects.get(id=promotion_id) if promotion_id else None
        offre.titre = titre
        offre.description = description
        offre.prix = prix
        offre.image = image
        offre.date_debut = date_debut
        offre.date_fin = date_fin
        offre.categorie = categorie
        offre.promotion = promotion
        offre.save()
        return redirect('offers')
    else:
        return redirect('offers')

def delete_offer(request, offer_id):
    offre = get_object_or_404(Offre, id=offer_id)
    offre.delete()
    return redirect('offers')
# Create your views here.
