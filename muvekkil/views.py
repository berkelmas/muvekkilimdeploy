from django.shortcuts import render, redirect
from .models import User, Dava, Surec

from django.contrib.auth import logout

# Create your views here.
def home(request):
    if request.user.is_authenticated:

        u = User.objects.get(id= request.user.id)
        davalar= u.dava_set.all()
        context = { 'davalar' : davalar }
        return render(request, 'muvekkil/index.html', context)
    else:
        return redirect('login')

def davadetay(request, id):

    if request.user.is_authenticated:
        user = request.user
        davalar = user.dava_set.all()
        dava_ids = []

        for dava in davalar:
            dava_ids.append(dava.id)

        if id in dava_ids:
            davaGetir = Dava.objects.get(id=id)
            surecGetir = davaGetir.surec_set.all()
            context = {'dava' : davaGetir,
                       'surecler' : surecGetir}
            return render(request, 'muvekkil/davadetay.html', context)

        else:
            return redirect('/')

    else:
        return redirect('login')

def auth_logout(request):
    logout(request)
    return redirect('login')