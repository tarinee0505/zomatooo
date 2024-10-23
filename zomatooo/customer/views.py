from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .forms import *
from master.models import *
from .models import *
from django.core.mail import send_mail
import random
# Create your views here.


def home(request):
    un = request.session.get('username')
    if un:
        user_object = User.objects.get(username=un)
        d = {'UO':user_object}
        return render(request, 'home.html', d)
    return render(request, 'home.html')

def customer_registration(request):
    ECFO = CustomerForm
    d = {'ECFO':ECFO}
    if request.method == 'POST':
        CFDO = CustomerForm(request.POST)
        if CFDO.is_valid():
            pw = CFDO.cleaned_data['password']
            MCFDO = CFDO.save(commit=False)
            MCFDO.set_password(pw)
            MCFDO.save()
            message=f"Hello {CFDO.cleaned_data.get('first_name')} \nWelcome to Zomatooo \nYour registration is done successfully\nThanks \nRegards"
            email=CFDO.cleaned_data.get('email')
            send_mail('Registration',message,'chandanchoudhury641@gmail.com',[email],fail_silently=False)
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('invalid data')
    return render(request,'customer_registration.html',d)


def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('invalid data')
    return render(request,'user_login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def customer_menu(request, type):
    if type == 'veg':
        items = Item.objects.filter(item_type='veg')
    elif type == 'non-veg':
        items = Item.objects.filter(item_type='Non-Veg')
    elif type == 'all':
        items = Item.objects.all()
    d = {'items':items}
    return render(request, 'customer_menu.html', d)
    

def addtocart(request):
    if request.method == 'POST':
        item_pk = request.POST.get('itempk')
        item_object = Item.objects.get(item_id=item_pk)
        UO = User.objects.get(username = request.session['username'])
        name = item_object.item_name
        price = item_object.item_price
        qty = request.POST.get('qty')
        CO = Cart(cart_id=UO, name=name, price=price, qty=qty)
        CO.save()
        return HttpResponse('Add Successfully')
    
    

def cart(request):
    CO = Cart.objects.all()
    un = request.session['username']
    CCI = list(filter(lambda i: i.cart_id.username == un, CO))
    d = {'items':CCI}
    return render(request,'cart.html',d)


def change_password(request):
    if request.method == 'POST':
        np= request.POST.get('np')
        cp= request.POST.get('cp')
        if cp!=np:
            return HttpResponse("Password doesn't match /n Reconfirm Your Password")
        send_otp=str(random.randint(100000,999999))
        my_mail='chandanchoudhury641@gmail.com'
        un=request.session['un']
        UO=User.objects.get(username=un)
        send_mail('OTP',send_otp,my_mail,[UO.email],fail_silently=False)
        request.session['cp']=cp
        request.session['otp']=send_otp
        return render(request,'otp.html')
        
    return render (request,'change.html')

def otp(request):
    if request.method =='POST':
        get_otp=request.POST.get('otp')
        un=request.session['un']
        send_otp=request.session['otp']
        if un is None or send_otp is None:
            return HttpResponse('Session data not found. Please try again.')
        if get_otp==str(send_otp):
            UO=User.objects.get(username=un)
            UO.set_password(request.session['cp'])
            UO.save()
            return HttpResponse('Password_changed')
        return HttpResponse(send_otp)
    return render (request,'otp.html')