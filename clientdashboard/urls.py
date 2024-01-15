from django.urls import path
from . import views
urlpatterns = [
    path('', views.accuile_page, name="clientdashboard"),
    path('settings', views.settings_page, name="clientsettings"),
    path('contactus', views.contactus_page, name="clientcontactus"),
]