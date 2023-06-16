
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
import time ,datetime
import random
import cryptocompare
from django.contrib.auth.decorators import login_required
from tronpy import Tron
from tronpy.keys import PrivateKey

# Create your views here.


def home(request):
    username = request.user.username

    d={'username':username}
    return render(request,'index.html',d)

def signup(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'signup.html',d)

def signin(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'signin.html',d)

def panel(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'panel.html',d)

def panelguest(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'panelguest.html',d)

def psyjournal(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'psyjournal.html',d)

def edujournal(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'edujournal.html',d)

def tests(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'tests.html',d)