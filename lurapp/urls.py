from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about,name='about'),
    path('Christmas', views.Christmas,name='Christmas'),
    path('contact', views.contact,name='contact'),
    path('Diwali', views.Diwali,name='Diwali'),
    path('gallery', views.gallery,name='gallery'),
    path('independence', views.independence,name='independence'),
    path('index', views.index,name='index'),
    path('Newyear', views.Newyear,name='Newyear'),
    path('others', views.others,name='others'),
    path('Republic', views.Republic,name='Republic'),
    path('service', views.service,name='service'),
    path('Login', views.Login,name='Login'),
    path('signup', views.signup,name='signup'),
    path('websitedesign', views.websitedesign,name='websitedesign'),
    path('uiuxdesign', views.uiuxdesign,name='uiuxdesign'),
    path('digitalmarketing', views.digitalmarketing,name='digitalmarketing'),
    path('accounts', views.accounts,name='accounts'),
    path('projectdesign',views.projectdesign,name='projectdesign'), 
    path('mobileapp', views.mobileapp,name='mobileapp'),

    path('secretarialservice', views.secretarialservice,name='secretarialservice'),
    path('otherservices', views.otherservices,name='otherservices'),
    path('payrollservice', views.payrollservice,name='payrollservice'),
    path('accountingservice', views.accountingservice,name='accountingservice'), 
    path('h1bvisa', views.h1bvisa,name='h1bvisa'),






    # path('indexcopy', views.indexcopy,name='indexcopy'),

]