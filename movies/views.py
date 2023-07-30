from django.shortcuts import render, redirect
from django.http import response
# Create your views here.


def Home(request):
    try:
        return render(request,'homepage.html')
    except Exception as ex:
        print("Exception in rendering Home page",str(ex))