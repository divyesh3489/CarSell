from django.contrib import admin
from .models import Carbrand, Carmodel, CarData, CarImage
# Register your models here.
admin.site.register(Carmodel)
admin.site.register(Carbrand)
admin.site.register(CarData)
admin.site.register(CarImage)
