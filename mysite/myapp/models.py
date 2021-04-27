from django.db import models

# Create your models here.
class Films(models.Model):
    name = models.CharField(max_length=100)
    url_film = models.URLField()
    description = models.CharField(max_length=500)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    url_cover = models.URLField()
    num_stars = models.DecimalField()

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    type_user = models.BooleanField()