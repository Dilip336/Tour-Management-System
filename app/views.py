from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Image
from .models import Contact

#from .forms import CustomerRegistrationForm


# Create your views here.
def home(request):
	pics = Image.objects.all()
	if request.method=="POST":
		#contact.contact()
		 name=request.POST.get('name')
		 email=request.POST.get('email')
		 subject=request.POST.get('subject')
		 #contact.name=name
		 #contact.email=email
		 #contact.subject=subject
		 #Contact.save()
		 print(name, email, subject)
		 #contact = contact(name=name, email=email, subject=subject)
		 contact = Contact(name=name, email=email, subject=subject)
		 contact.save()

		 return HttpResponse("Thank you for your response, our team will catch you soon")
	return render(request, 'app/index.html', {"pics":pics})


def about(request):
    return render(request, 'app/about.html')

def booking(request):
    return render(request, 'app/booking.html')


def photo(request):
    return render(request, 'app/photo.html')

def customerregistration(request):
    return  render(request,'app/customerregistration.html' )
    
def loginn (request):
    return render(request, 'app/login.html') 


def Search (request):
	render 
	