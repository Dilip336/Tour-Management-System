from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Image
from .models import Contact
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



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
	if request.method =='POST':
		print("hello")
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			form =UserCreationForm()
	else:
		form = UserCreationForm()	
	return  render(request,'app/customerregistration.html', {'form':form})
    
def loginn (request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse("Thanks for Login")
		
		# form = AuthenticationForm(request=request,user=request.POST)
		# if form.is_valid():
		# 	usr = form.cleaned_data['username']
		# 	pwdd = form.cleaned_data['password']
		# 	userss = authenticate(username=usr,password=pwdd)
		# 	if userss is not None:
		# 		login(request, userss)
		# 		return HttpResponse("login success")

	
	form = AuthenticationForm()
	return render(request, 'app/login.html',{'form':form}) 

	


	