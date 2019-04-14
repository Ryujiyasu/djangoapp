from django.shortcuts import render
from django.http import HttpResponse
from artistsell.models import Artistsell
from django.views.generic import ListView

def sum(request,artist,yearmonth):
    return HttpResponse("Hello, world."+artist+str(yearmonth))

class MyListView(ListView):

    model = Artistsell
    template_name = 'artistsell/mymodel_list.html'
