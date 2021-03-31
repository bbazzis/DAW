from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('login_user', views.login_user, name='login_user'),
 path('login_admin', views.login_admin, name='login_admin'),
 path('nuevas_peliculas', views.nuevas_peliculas, name='nuevas_peliculas'),
]
