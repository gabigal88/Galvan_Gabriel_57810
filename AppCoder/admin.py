from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
    list_filter=("nombre",)
    list_display=("nombre","apellido","identificacion","email","telefono")

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Bicicleta)
admin.site.register(Accesorios)
admin.site.register(Rental)
admin.site.register(Circuito)

# Register your models here.
