from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json

from .models import Referee,Judge,Examinar,Author,Team,BlackBelt,Affiliation,Gallery


def index(request):
    team = Team.objects.all()
    referee = Referee.objects.all()
    judge = Judge.objects.all()
    examinar = Examinar.objects.all()
    author = Author.objects.all()
    blackbelt =BlackBelt.objects.all()
    affiliation = Affiliation.objects.filter().order_by('-id')[:1]
    context = {
        "is_index" : True,
        "team":team,
        "referee":referee,
        "judge":judge,
        "examinar":examinar,
        "author":author,
        "blackbelt":blackbelt,
        "affiliation":affiliation,
        
    }
    return render(request, 'index.html',context)

def about(request):
    context = {
        "is_about" : True,
    }
    return render(request, 'about.html',context)

def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        "is_gallery" : True,
        "gallery":gallery,
    }
    return render(request, 'gallery.html',context)

def contact(request):
    context = {
        "is_contact" : True,
    }
    return render(request, 'contact.html',context)

