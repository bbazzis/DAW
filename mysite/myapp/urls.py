from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
urlpatterns = [
 path('', views.index, name='index'),
 path('get_login', views.get_login, name="get_login"),
 path('login_user', views.login_user, name='login_user'),
 path('login_admin', views.login_admin, name='login_admin'),
 path('new_film', views.new_film, name='new_film'),
 path('new_user', views.new_user, name='new_user'), 
 path('new_admin', views.new_admin, name='new_admin'),
 path('modify_users', views.modify_users, name='modify_users'),
 path('films', views.films, name='films'),
 path('add_film', views.add_film, name="add_film"),
 path('add_user', views.add_user, name="add_user"),
 path('add_admin', views.add_admin, name="add_admin"),
 path('film/<str:nameFilm>/', views.film, name="film"),
 path('get_logout', views.get_logout, name="get_logout"),
 path('del_user/<str:username>', views.del_user, name="del_user"),
 path('mod_user/<str:username>', views.mod_user, name="mod_user"),
 path('modify_films', views.modify_films, name="modify_films"),
 path('del_film/<str:name_film>', views.del_film, name="del_film"),
 path('mod_film/<str:name_film>', views.mod_film, name="mod_film"),
 path('films_user', views.films_user, name='films_user'),
 path('film_user/<str:nameFilm>/', views.film_user, name="film_user"),
 path('search', views.search, name="search"),
 path('search_user', views.search_user, name="search_user")
]

