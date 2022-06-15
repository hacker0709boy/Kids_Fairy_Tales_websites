from django.shortcuts import render
from django.http import HttpResponse
from .models import *


from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.




def index(request):
	index = English.objects.all()
	context = {'index':index}

	return render(request, 'websites/index.html', context)





def about(request):
	about = About.objects.all()
	context = {'about': about}
	return render(request, 'websites/about.html', context)










def contact(request):
	if request.method == 'POST':

		name = request.POST.get('name'),
		email = request.POST.get('email'),
		phone = request.POST.get('phone'),
		subject = request.POST.get('subject'),
		message = request.POST.get('message'),

		send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)

		
		return render(request, 'websites/send_template.html', {'name': name})
	else:
		return render(request, 'websites/contact.html', {})



def work(request):
	context = {}
	return render(request, 'websites/work.html', context)



def snow(request):
	context = {}
	return render(request, 'websites/snow.html', context)









def indextm(request):
	indextm = Post.objects.all()
	context = {'indextm':indextm}
	return render(request, 'websites/indextm.html', context)


def abouttm(request):
	abouttm = Abouttm.objects.all()
	context = {'abouttm': abouttm}
	
	return render(request, 'websites/abouttm.html', context)

def contacttm(request):
	context = {}
	return render(request, 'websites/contacttm.html', context)


def worktm(request):
	context = {}
	return render(request, 'websites/worktm.html', context)







