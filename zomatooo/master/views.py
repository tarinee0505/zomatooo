from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
# Create your views here.
def master_registration(request):
    EMFO = MasterForm
    d = {'EMFO':EMFO}
    if request.method == 'POST':
        MFDO = MasterForm(request.POST)
        if MFDO.is_valid():
            pw = MFDO.cleaned_data['password']
            MMFDO = MFDO.save(commit=False)
            MMFDO.set_password(pw)
            MMFDO.is_staff = True
            MMFDO.save()
            return HttpResponseRedirect(reverse('master_login'))
        return HttpResponse('invalid data')
    return render(request, 'master_registration.html',d)


def master_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un,password=pw)
        if AUO :
            if AUO.is_active:
                if AUO.is_staff:
                    login(request, AUO)
                    request.session['usernamem'] =un
                    return HttpResponseRedirect(reverse('home'))
                return HttpResponse('not a staff')
            return HttpResponse('User in not active')
        return HttpResponse('invalid Credentials')
    return render(request,'master_login.html')


def additem(request):
    EIFO = ItemForm()
    d = {'EIFO':EIFO}
    if request.method == 'POST' and request.FILES:
        IFDO = ItemForm(request.POST, request.FILES)
        if IFDO.is_valid():
            IFDO.save()
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('Invalid Data')

    return render(request, 'additem.html', d)


def menu(request):
    items = Item.objects.all()
    d = {'items':items}
    return render(request, 'menu.html', d)


def update(request, pk):
    item_object = Item.objects.get(item_id=pk)
    d = {'EIFO': item_object}
    print(d['EIFO'])
    return render(request, 'additem.html', d)
    

def master_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))