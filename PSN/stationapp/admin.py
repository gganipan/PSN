from django.contrib import admin
from . models import Station, History, Repair

# Register your models here.
admin.site.register(Station)
admin.site.register(History)
admin.site.register(Repair)
