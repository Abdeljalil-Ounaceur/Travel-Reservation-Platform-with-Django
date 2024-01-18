from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from pages.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, redirect
from pages.models import Categorie


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
    return render(request,'admindashboard/newoffer.html')

def offers_page(request) :
    return render(request,'admindashboard/offers.html')

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

# Create your views here.
