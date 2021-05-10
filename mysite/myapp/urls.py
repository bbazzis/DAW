from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('get_login', views.get_login, name="get_login"),
 path('login_user', views.login_user, name='login_user'),
 path('login_admin', views.login_admin, name='login_admin'),
 path('new_film', views.new_film, name='new_film'),
 path('new_user', views.new_user, name='new_user'), 
 path('new_admin', views.new_admin, name='new_admin'),
 path('modify_user', views.modify_user, name='modify_user'),
 path('films', views.films, name='films'),
 path('add_film', views.add_film, name="add_film"),
 path('add_user', views.add_user, name="add_user"),
 path('add_admin', views.add_admin, name="add_admin"),
 path('film', views.film, name="film"),

]

