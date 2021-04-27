from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.template import loader
from myapp.models import Films, Users

def index(request):
    template = loader.get_template("myapp/index.html")
    return HttpResponse( template.render())

def login_user(request):
    context={}
    return render(request,"myapp/login_user.html", context)

def login_admin(request):
    context={}
    return render(request,"myapp/login_admin.html", context)

def new_film(request):
    context={}
    return render(request,"myapp/new_film.html", context)

def new_user(request):
    context={}
    return render(request,"myapp/new_user.html", context)

def modify_user(request):
    context={}
    return render(request,"myapp/modify_user.html", context)

def films(request):
    context={}
    return render(request,"myapp/films.html", context)

def add_film(request):
    if request.method == "POST":
        name_film = request.POST('name_film')
        url_film = request.POST('url_film')
        description = request.POST('description')
        year = request.POST('year')
        director = request.POST('director')
        actors = request.POST('actors')
        url_cover = request.POST('url_cover')
        num_stars = request.POST('num_stars')
        new_film = Films(name_film=name_film, url_film=url_film, description=description, year=year, director=director, actors=actors, url_cover=url_cover, num_stars=num_stars)
        new_film.save()

    return HttpResponse("done")