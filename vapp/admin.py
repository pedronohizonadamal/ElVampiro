from django.contrib import admin
from paramiko import PKey

from .models import Vampiro

# Register your models here.

class VampiroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'habita', 'email')
    search_fields = ('nombre', 'habita')
    
    actions = ['cazar']
    
    def cazar(self, request, queryset):
        for q in queryset:
            h = q.get_habita()
            victima = q.get_victima()
            bp = q.get_bajas_pendientes()
            vampiro = Vampiro.objects.filter(pk=h)
            if victima and bp > 0:
                vampiro.update(victima=victima.get_victima())
                Vampiro.objects.filter(pk=victima.get_habita()).delete()
                vampiro.update(bajas=q.get_bajas() + 1)
                vampiro.update(bajas_noche=q.get_bajas_noche() + 1)
                vampiro.update(bajas_pendientes=0)

admin.site.register(Vampiro, VampiroAdmin)
#admin.site.unregister(Vampiro)