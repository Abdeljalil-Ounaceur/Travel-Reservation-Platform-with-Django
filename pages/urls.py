from django.urls import path
from . import views
urlpatterns = [
    path('', views.accuile_page, name="accuilepage"),
    path('login',views.login_SingUp_Page, name="login_SingUp_Page"),
    path('contact-us',views.contact_us_page, name="contact_us_page"),
    path('about-us',views.about_us_page, name="about_us_page"),
    path('package',views.package_page, name='package_page'),
    path('offers',views.offers_page, name='offers_page'),
    path('login_verification',views.login_verification, name='login_verification'),
]
