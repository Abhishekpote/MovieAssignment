from django.contrib import admin
from .models import Movies,Favourites,Genre
# Register your models here.


admin.site.register(Movies)
admin.site.register(Genre)
admin.site.register(Favourites)