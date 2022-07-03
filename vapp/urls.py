from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='castillo'),
    path('baja', views.baja, name='baja'),
]