from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.home,name='about'),
    path('contactUs',views.contactUs,name='contactUs'),   
]