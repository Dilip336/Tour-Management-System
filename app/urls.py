from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('gallery/', views.gallery, name="gallery"),
    path('booking/', views.booking, name=" booking"),
    path('aboutus/', views.aboutus, name='About'),
    path("destination/", views.destination, name="destination"),
    path('search', views.search, name="search"),
   
]
 