from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from .models import Referee,Judge,Examinar,Author,Team


def index(request):
    team = Team.objects.all()
    referee = Referee.objects.all()
    judge = Judge.objects.all()
    examinar = Examinar.objects.all()
    author = Author.objects.all()
    context = {
        "is_index" : True,
        "team":team,
        "referee":referee,
        "judge":judge,
        "examinar":examinar,
        "author":author,
    }
    return render(request, 'index.html',context)