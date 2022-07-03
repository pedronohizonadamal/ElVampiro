from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Vampiro, BajaRequest

def home(request):
    return render(request, 'castillo.html')

def baja (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        vict = request.POST.get('vict')
        
        for vamp in Vampiro.objects.filter(email = email):
            if vamp.get_victima().get_habita() == vict:
                if vamp.get_bajas_pendientes() == 0:
                    Vampiro.objects.filter(email = email).update(bajas_pendientes = 1)
                    baja = BajaRequest(habitaVamp=vamprio.get_habita(), habitaVict=vict)
                    baja.save()
                    print('Baja requested')
                return redirect('/castillo')     
        
    return render(request, 'baja.html')
                    




# Create your views here.
