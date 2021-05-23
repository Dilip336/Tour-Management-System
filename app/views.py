
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Booking
from .models import Search



#from .forms import CustomerRegistrationForm


# Create your views here.
def home(request):
	# Search.objects.all().delete()

	# Search1 = Search(upperclass="col",lowerclass="col1",title="Chitwan", description="At the foot of the Himalayas, Chitwan is one of the few remaining undisturbed vestiges of the 'Terai' region.", image="/static/app/images/chitwan.jpg")
	# Search1.save()

	# Search2 = Search(upperclass="col",lowerclass="col2",title = "Pokhara",description = "Pokhara is a city on Phewa Lake, in central Nepal. It’s known as a gateway to the Annapurna Circuit.",image = "/static/app/images/pokhara.jpg")
	# Search2.save()

	# Search3 = Search(upperclass="",lowerclass="col1",title = "Lumbini",description = "Siddhartha Gautama, the Lord Buddha, was born in 623 B.C. in the famous gardens of Lumbini, which soon became a place of pilgrimage.",image = "/static/app/images/lumbini.jpg")
	# Search3.save()

	# Search4 = Search(upperclass="",lowerclass="col2",title = "Sagarmatha",description = "Mount Everest is Earth's highest mountain above sea level, located in the Mahalangur Himal sub-range of the Himalayas.",image = "/static/app/images/sagarmatha.jpg")
	# Search4.save()

	# Search5 = Search(upperclass="col",lowerclass="",title = "Nyatapola temple - Bhaktapur",description = "Nyatapola Temple is a 5-storeyed Hindu temple. Meaning is Five Storeys Roofed Temple. Pagoda Style temple located in Bhaktapur, Nepal.",image = "/static/app/images/kathmandu valley.jpeg")
	# Search5.save()
	Context={
		"Content": Search.objects.all()

	}
	return render(request, 'app/index.html', Context)
def gallery(request):
	return render(request, 'app/gallery.html')
def aboutus(request):
	return render(request, 'app/aboutus.html')
def destination(request):
	return render(request, 'app/destination.html')
#search funct	
def search(request):
	query = request.POST['s']
	obj = Search.objects.all()
	current_obj= []
	for object in obj:
		if query.lower() in str(object.title).lower():
			current_obj.append(object)
	Context={
		"Content": current_obj
	}
	return render(request, 'app/index.html', Context)



def booking(request):
	if request.method=="POST":
		#contact.contact()
		 travellingform=request.POST.get('travellingfrom')
		 travellingto=request.POST.get('travellingto')
		 departing=request.POST.get('departing')
		 returing=request.POST.get('returing')
		 adults=request.POST.get('adults')
		 childern=request.POST.get('children')
		 traveltypes =request.POST.get('traveltypes') 
		 print(travellingform, travellingto,  departing, returing,  adults, childern )
		 #contact = contact(name=name, email=email, subject=subject)
		 Booking1 = Booking(travellingform=travellingform,travellingto=travellingto, departing=departing, returing=returing,adults=adults,childern=childern,traveltypes=traveltypes)
		 Booking1.save()

		 return HttpResponse("Thank you for your response, our team will catch you soon")
	return render(request, 'app/booking.html')


