from django.shortcuts import render, redirect
from django.http import response
from .models import *
# Create your views here.
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, request,Http404

def Home(request):
    try:
        mov = Movies.objects.all()
        print(mov)
        return render(request,'homepage.html')
    except Exception as ex:
        print("Exception in rendering Home page",str(ex))


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