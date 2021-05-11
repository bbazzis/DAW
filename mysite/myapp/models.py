from django.db import models
from django.contrib.auth.models import User, Permission, Group
# Create your models here.
class Films(models.Model):
    name_film = models.CharField(max_length=100)
    url_film = models.URLField()
    description = models.CharField(max_length=500)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    url_cover = models.URLField()
    num_stars = models.FloatField()
