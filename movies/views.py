from django.shortcuts import render, redirect
from django.http import response
from .models import *
from django.contrib import messages
# Create your views here.
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, request,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def Home(request):
    try:
        if request.method == "POST":
            details = request.POST
            username = details['username']
            password = details['password']

            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
            else:
                messages.add_message(request, messages.INFO, "Invalid credentials!!!!")
            return redirect("/")
        return render(request,'homepage.html')
    except Exception as ex:
        print("Exception in rendering Home page",str(ex))


def logout_user(request):
    try:
        logout(request)
        return render(request,'homepage.html')
    except Exception as ex:
        redirect("/")

def signUp(request):
    try:
        if request.method == "POST":
            details = request.POST
            message = ""
            if details["username"] == "":
                message = "Invalid Username" 
            elif details["password"] == "": 
                message = "Invalid Password"
            elif details["email"] =="" and "@" not in details["email"]:
                message = "Invalid Email"
            elif details["firstname"] == "":
                message = "Firstname required"
            elif details["lastname"] == "":
                message = "Lastname required"


            if message != "":
                messages.add_message(request, messages.INFO, message)
                return redirect("Signup")
            else:
                print("details",details)
                user = User.objects.create_user(username = details["username"],password = details["password"], email = details["email"], first_name = details["firstname"], last_name = details["lastname"])
                user.save()
                return redirect("/")
        
        return render(request,"register.html")
    except Exception as ex:
        print("Exception in Registering",str(ex))


class MovieList(generic.ListView):
    try:
        model = Movies
        template_name = 'movieList.html'

        def get_context_data(self, **kwargs):
            context = super(MovieList,self).get_context_data(**kwargs)
            return context
    except:
        raise Http404("Sorry!!! Something went wrong")
    
class MovieDetail(generic.DetailView):
    try:
        model = Movies
        template_name = 'movieDetail.html'

        def get_context_data(self, **kwargs):
            context = super(MovieDetail,self).get_context_data(**kwargs)
            return context
    except:
        raise Http404("Sorry!!! Something went wrong")