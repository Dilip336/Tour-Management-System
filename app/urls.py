from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name=" about page"),
    path('booking/', views.booking, name=" booking"),
    path('photo/', views.photo, name="photo"),
    path('customerregistration/', views.customerregistration, name = "customerregistration"),
    path('loginn/', views.loginn, name="login"),
   
]
 