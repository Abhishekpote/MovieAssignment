from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length = 200)
    title = models.CharField(max_length=1000)
    released_date = models.DateField()
    budget = models.CharField(max_length= 200)
    cast = models.CharField(max_length= 1000)
    synopsis = models.TextField(null=True,blank=True)
    thumbnail = models.ImageField(upload_to='MovieThumbnails/',blank=True,null=True)
    genre = models.ForeignKey(Genre,on_delete=models.DO_NOTHING)
    runtime = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Favourites(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movies)

    def __str__(self):
        return self.user.username
