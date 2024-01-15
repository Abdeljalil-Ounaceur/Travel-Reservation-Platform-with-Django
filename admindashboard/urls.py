from django.urls import path
from . import views
urlpatterns = [
    path('', views.accuile_page, name="admindashboard"),
    path('category', views.category_page, name="category"),
    path('client', views.client_page, name="client"),
    path('contactus', views.contactus_page, name="contactus"),
    path('newcategory', views.newcategory_page, name="newcategory"),
    path('newoffer', views.newoffer_page, name="newoffer"),
    path('offers', views.offers_page, name="offers"),
    path('settings', views.settings_page, name="settings"),

]
