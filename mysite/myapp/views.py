from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.template import loader
from myapp.models import *
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.decorators import login_required
def index(request):
    template = loader.get_template("myapp/index.html")
    return render(request, 'myapp/index.html')
    
def get_login(request):
    context={}
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            if user.has_perm('myapp.add_users'):
                return redirect('login_admin')
            else:
                return redirect('login_user')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'myapp/index.html', {'login_failed': True})

@login_required
def login_user(request):
    context={}
    return render(request,"myapp/login_user.html", context)
@login_required
def login_admin(request):
    context={}
    return render(request,"myapp/login_admin.html", context)
@login_required
def new_film(request):
    context={}
    return render(request,"myapp/new_film.html", context)
@login_required
def new_user(request):
    context={}
    return render(request,"myapp/new_user.html", context)
@login_required
def new_admin(request):
    context={}
    return render(request,"myapp/new_admin.html", context)
@login_required
def modify_user(request):
    context={}
    return render(request,"myapp/modify_user.html", context)
@login_required
def films(request):
    context={}
    if request.method == 'GET':
        films = Films.objects.all()
    return render(request,"myapp/films.html", {'films':films})
@login_required
def film(request, nameFilm):
    context={}
    films = Films.objects.get(name_film = nameFilm)
    return render(request,"myapp/film.html", {'films':films})
@login_required
def add_film(request):
    context={}
    if request.method == "POST":
        name_film = request.POST['name_film']
        url_film = request.POST['url_film']
        description = request.POST['description']
        year = request.POST['year']
        director = request.POST['director']
        actors = request.POST['actors']
        url_cover = request.POST['url_cover']
        num_stars = request.POST['num_stars']
        new_film = Films(name_film=name_film, url_film=url_film, description=description, year=year, director=director, actors=actors, url_cover=url_cover, num_stars=num_stars)
        new_film.save()

    return render(request,"myapp/new_film.html", context)
@login_required
def add_user(request):
    context={}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_to_add = User.objects.create_user(username, email, password)
        user_to_add.save()
        users, created=Group.objects.get_or_create(name="Users")
        
        user_to_add.groups.add(users)

    return render(request,"myapp/new_user.html", context)
@login_required
def add_admin(request):
    context={}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        admin_to_add = User.objects.create_user(username, email, password)
        admin_to_add.save()
        admins, created=Group.objects.get_or_create(name="Admins")
        p1=Permission.objects.get(codename="add_users")
        admins.permissions.add(p1)
        admin_to_add.groups.add(admins)

    return render(request,"myapp/new_admin.html", context)
@login_required
def get_logout(request):
    context={}
    logout(request)
    return render(request, 'myapp/logout.html', context)