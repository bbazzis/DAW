from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('login_user', views.login_user, name='login_user'),
 path('login_admin', views.login_admin, name='login_admin'),
 path('new_film', views.new_film, name='new_film'),
 path('new_user', views.new_user, name='new_user'),
 path('modify_user', views.modify_user, name='modify_user'),
]
