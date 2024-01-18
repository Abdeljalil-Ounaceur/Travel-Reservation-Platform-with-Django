from django.urls import path
from . import views
urlpatterns = [
    path('', views.accuile_page, name="accuilepage"),
    path('login',views.login_SingUp_Page, name="login_SingUp_Page"),
    path('contact-us',views.contact_us_page, name="contact_us_page"),
    path('about-us',views.about_us_page, name="about_us_page"),
    path('package',views.package_page, name='package_page'),
    path('offers',views.offers_page, name='offers_page'),
    path('login_validation',views.login_validation, name='login_validation'),
    path('signup_validation',views.signup_validation, name='signup_validation'),
    path('Code_validation',views.get_verificaioncode, name='Code_validation'),
    path('signup_validation1',views.email_validation, name='signup_validation1'),
    path('testmail',views.simple_mail),
]
