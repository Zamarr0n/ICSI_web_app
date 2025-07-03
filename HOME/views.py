from django.shortcuts import redirect, render
from django.http import HttpResponse
from ICSI import settings
from .models import *
from django.views.generic import ListView, DetailView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
import ssl
# Create your views here.
def index(request):
    return render(request, "HOME/index.html")

def marcas(request):
    return render(request, 'HOME/marcas.html');

def servicios(request):
    if request.method == "POST":
        subject = request.POST["subject"]
        name = request.POST["Nombre"]
        last_name = request.POST["Apellido"]
        email = request.POST["email"]
        whatsapp = request.POST["Whatsapp"]
        contact = request.POST["contact"]
        purpose = request.POST['Proposito']
        comments = request.POST["comments"]
        template = render_to_string('email_template.html',{
            'subject': subject,
            'nombre': name,
            'lastName': last_name,
            'email': email,
            'whatsapp': whatsapp,
            'contact': contact,
            'purpose': purpose,
            'comments': comments
        } )
        
        email = EmailMessage(
            subject = subject,
            body = template,
            from_email = settings.EMAIL_HOST_USER,
            to = ['icsiwebapp@gmail.com','gerencia@icsalan.com', 'cestzamarron@gmail.com']
        )
        email.fail_silently = False
        print("Apunto de enviarse")
        email.send()
        messages.success(request, 'En breve seras contactactado por nuestro equipo ')
        
    return render(request, 'HOME/servicios.html');






def nosotros(request):
    return render(request, 'HOME/nosotros.html');

class blog (ListView):
    model = Blog
    template_name = 'HOME/blog.html'

class DetailBlog(DetailView):
    model = Blog
    template_name = 'HOME/blog_complete.html'


