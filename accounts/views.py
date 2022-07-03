from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth

from vapp.models import BajaRequest, Vampiro

# Create your views here.

def register (request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        room = request.POST.get('room')
        

        
        if Vampiro.objects.filter(habita=room).exists():
            print('Room taken')
        elif Vampiro.objects.filter(email=email).exists():
            print('Email taken')
        else:
        
            vampiro = Vampiro(nombre=name, email=email, habita=room)
            vampiro.save();
            print('User created')
        
        return redirect('/castillo')
    return render(request, 'register.html')

        

def login (request):
    return render(request, 'login.html')