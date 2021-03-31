from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("myapp/index.html")
    return HttpResponse( template.render())

def login_user(request):
    context={}
    return render(request,"myapp/login_user.html", context)

def login_admin(request):
    context={}
    return render(request,"myapp/login_admin.html", context)

def nuevas_peliculas(request):
    context={}
    return render(request,"myapp/nuevas_peliculas.html", context)