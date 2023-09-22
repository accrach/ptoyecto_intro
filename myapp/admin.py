from django.contrib import admin
from .models import Abecedario, Categoria, Explicaciones, Actividades

''' Credenciales user admin'''
# Username: admin
# Passwd: admin

''' Vista de tablas mediante el user admin (Se visualiza en la página de Django)'''

admin.site.register(Abecedario)
admin.site.register(Categoria)
admin.site.register(Explicaciones)
admin.site.register(Actividades)


