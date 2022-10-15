from django.contrib import admin
from django.urls import path
from order import views

urlpatterns = [
    path("",views.home, name='demo'),
    path('sell',views.sell, name='sell'),
    path('register',views.register, name='register'),
    # path('order/booked',views.booked, name='booked'),
    # path("about", views.about, name='about'),
    # path("services", views.service, name="sevices"),
    path("contact", views.contact, name="contact"),
    path('order',views.orderaction, name ='order'),
    path('home1',views.home1, name='home1'),
]