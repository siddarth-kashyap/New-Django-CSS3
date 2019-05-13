from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf.urls import url
from django.views.generic import TemplateView
from Content.forms import ContactForm

# Create your views here.
class home(TemplateView):
    """THe Home PAGE """
    template_name = 'home.html'
    #return HttpResponse('Home Page!')

class aboutus(TemplateView):
    """THe About us PAGE """
    template_name = 'aboutus.html'

class policy(TemplateView):
    """Testing PAGE """
    template_name = 'policy.html'

def emailView(request):
    if request.method =='GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form':form})

def successView(request):
    return render(request, "submit.html")
