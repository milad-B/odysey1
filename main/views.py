
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
import jdatetime
from django.http import JsonResponse




# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'



def home(request):
    username = request.user.username
    bannerimg = Homepage.objects.get(selected=1).img_url
    stickies = Sticky.objects.filter(homepage__selected=1)

    d={'username':username,
       'bannerimg':bannerimg,
       'stickies':stickies,
       }
    return render(request,'index.html',d)

def signup(request):
    username = request.user.username
    if request.method == 'POST':

        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password= request.POST.get('password')

        User.objects.create_user(username=str(username),email=email,password=password,first_name=name)
        user = authenticate(username=username, password=password)
        Profile.objects.create(user = user , name=name , number =int(username) )
        
    return render(request , 'signup.html')


def panel(request):
    if is_ajax(request) and request.method == "POST":
        listofhour=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        d = str(request.POST.get('date')).split('/')
        reservedata = jdatetime.date(int(d[0]),int(d[1]),int(d[2])).togregorian()

        day = Reserve.objects.filter(date=reservedata ,confirm=1)
        for d in day:
            h = int(str(d.hour).split(':')[0])

            if h in listofhour:
                listofhour.remove(h)
            print(h)

           
        return JsonResponse(listofhour, safe=False)
    



    if  request.method == 'POST':
        username = request.user.username
        oup = Profile.objects.get(user=request.user)
        advicehistory = Reserve.objects.filter(user=request.user, service='advice',confirm=1)
        therapyhistory = Reserve.objects.filter(user=request.user, service='therapy',confirm=1)

        
        d = str(request.POST.get('reservedate')).split('/')
        reservedata = jdatetime.date(int(d[0]),int(d[1]),int(d[2])).togregorian()
        h = int(request.POST.get('times'))
        if h<10:
            reservehour = '0'+ str(h)+':00'
        else:
            reservehour = str(h)+':00'

        service = request.POST.get('service')
        detail = request.POST.get('details')

        if Reserve.objects.filter(user=request.user, service=service,confirm=2):
            pass
        else:
            Reserve.objects.create(user=request.user, service=service,detail=detail,date=reservedata , hour = reservehour ,confirm=2).save()
        

        
        try:
            lastpending = Reserve.objects.filter(user=request.user,confirm=2).first()
        except:
            lastpending = 0
        try:
            lastconfirmed = Reserve.objects.filter(user=request.user,confirm=1).first()
        except:
            lastconfirmed = 0
        try:
            lastdenied = Reserve.objects.filter(user=request.user,confirm=0).first()
        except:
            lastdenied = 0
        d={ 
            'username':username,
           'oup':oup,
           'advicehistory':advicehistory,
           'therapyhistory':therapyhistory,
           'lastpending':lastpending,
           'lastconfirmed':lastconfirmed,
           'lastdenied':lastdenied,

           }
        return render(request , 'panel.html',d)
    

    username = request.user.username
    oup = Profile.objects.get(user=request.user)
    advicehistory = Reserve.objects.filter(user=request.user, service='advice',confirm=1)
    therapyhistory = Reserve.objects.filter(user=request.user, service='therapy',confirm=1)

    try:
        lastpending = Reserve.objects.filter(user=request.user,confirm=2).first()
    except:
        lastpending = 0
    try:
        lastconfirmed = Reserve.objects.filter(user=request.user,confirm=1).first()
    except:
        lastconfirmed = 0
    try:
        lastdenied = Reserve.objects.filter(user=request.user,confirm=0).first()
    except:
        lastdenied = 0
    d={ 
            'username':username,
           'oup':oup,
           'advicehistory':advicehistory,
           'therapyhistory':therapyhistory,
           'lastpending':lastpending,
           'lastconfirmed':lastconfirmed,
           'lastdenied':lastdenied,

        }
    return render(request , 'panel.html',d)



def panelguest(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'panelguest.html',d)

def journal(request,sub):
    if request.user.username:
        username = request.user.username
        oup = Profile.objects.get(user=request.user)
    else:
        username = 'guest'
    
    

    if  request.method == 'POST':

        subject = request.POST.get('subject')
        postpk = request.POST.get('postpk')
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        post = Bpost.objects.get(pk=postpk, subject=subject)
        if request.user.username:
            username = request.user.username
            oup = Profile.objects.get(user=request.user)
            img = oup.img
            Comment(post=post, name=name, email=email, Comment=comment, img = img).save()
        else:
            username = 'guest'
            img = None
            Comment(post=post, name=name, email=email, Comment=comment).save()

    posts = Bpost.objects.filter(subject=sub)
    

    d={'posts':posts,
        'username':username,
        }
    return render(request , 'psyjournal.html',d)



def tests(request):
    username = request.user.username

    d={'username':username}
    return render(request , 'tests.html',d)