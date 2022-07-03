from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vampiro(models.Model):
    nombre = models.CharField(max_length=20, default=None, blank=True, null=True)
    habita = models.IntegerField(default = 0, primary_key=True)
    email = models.EmailField(default=None, blank=True, null=True)
    bajas = models.IntegerField(default=0)
    bajas_noche = models.IntegerField(default=0)
    bajas_pendientes = models.IntegerField(default=0)
    victima = models.ForeignKey('self', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    def __unicode__(self):
        return u'%s %d'%(self.nombre, self.habita)
    
    def __str__(self):
        return '%s %d'%(self.nombre, self.habita)
    
    def get_victima(self):
        return self.victima
    def get_bajas(self):
        return self.bajas
    def get_bajas_noche(self):
        return self.bajas_noche
    def get_bajas_pendientes(self):
        return self.bajas_pendientes
    def get_habita(self):
        return self.habita
    def set_victima(self, v):
        self.victima = v
    def set_bajas(self, b):
        self.bajas = b
    def set_bajas_noche(self, bn):
        self.bajas_noche = bn
    def set_bajas_pednientes(self, bp):
        self.bajas_pendientes = bp
    
class Muerto(models.Model):
    nombre = models.CharField(max_length=20, default=None, blank=True, null=True)
    habita = models.IntegerField(default = 0, primary_key=True)
    email = models.EmailField(default=None, blank=True, null=True)
    bajas = models.IntegerField(default=0)
    bajas_noche = models.IntegerField(default=0)
    bajas_pendientes = models.IntegerField(default=0)
    victima = models.ForeignKey('self', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    def __unicode__(self):
        return u'%s %d'%(self.nombre, self.habita)
    
    def __str__(self):
        return '%s %d'%(self.nombre, self.habita)
    
    def get_victima(self):
        return self.victima
    def get_bajas(self):
        return self.bajas
    def get_bajas_noche(self):
        return self.bajas_noche
    def get_bajas_pendientes(self):
        return self.bajas_pendientes
    def get_habita(self):
        return self.habita
    def set_victima(self, v):
        self.victima = v
    def set_bajas(self, b):
        self.bajas = b
    def set_bajas_noche(self, bn):
        self.bajas_noche = bn
    def set_bajas_pednientes(self, bp):
        self.bajas_pendientes = bp
    
class BajaRequest(models.Model):
    habitaVamp = models.IntegerField()
    habitaVict = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True, primary_key=True) 
