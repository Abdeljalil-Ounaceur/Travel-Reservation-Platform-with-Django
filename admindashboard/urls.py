from django.urls import path
from . import views
urlpatterns = [
    path('', views.accuile_page, name="admindashboard"),
    path('client', views.client_page, name="client"),
    path('offers', views.offers_page, name="offers"),
    path('category', views.category_page, name="category"),
    path('contactus', views.contactus_page, name="contactus"),
    path('settings', views.settings_page, name="settings"),
    path('newclient', views.newclient_page, name="newclient"),
    path('newcategory', views.newcategory_page, name="newcategory"),
    path('newoffer', views.newoffer_page, name="newoffer"),

    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('edit_client/<int:client_id>/', views.edit_client, name='edit_client'),
    path('create_client', views.create_client, name="create_client"),

    path('create_category', views.create_category, name="create_category"),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),

]
