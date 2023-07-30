
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from movies import views



urlpatterns = [
    path('', views.Home, name='Home'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)