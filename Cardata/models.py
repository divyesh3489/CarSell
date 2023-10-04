from django.db import models
import datetime
from location_field.forms.plain import PlainLocationField

IDE = [
    ((i+1)*100000, i+1) for i in range(0, 10)
]
KM = [
    ((i+1)*10000, (i+1)*10000) for i in range(0, 15)
]
KM.insert(0, ('', ''))
print(KM)
year = [
    (i, i) for i in range(2013, datetime.datetime.now().year+1)
]
owner = [('', ''), ('1st', '1st'), ('2nd', '2nd'),
         ('3rd', '3rd'), ('dealer', 'dealer')]
year.insert(0, ('', ''))
fule = [("CNG", "CNG"), ("Petrol", 'Petrol'), ("Diesel", 'Diesel')]
trans = [("Manual", "Manual"), ("Automatic", 'Automatic')]


class Carbrand(models.Model):
    def __str__(self) -> str:
        return self.carbrand
    carbrand = models.CharField(max_length=100)
class Carmodel(models.Model):
    def __str__(self) -> str:
        return self.carmodel
    carbrand = models.ForeignKey(Carbrand, on_delete=models.CASCADE, default=1)
    carmodel = models.CharField(max_length=100, default='')
    mileage = models.CharField(max_length=50, default='')
    doors = models.IntegerField()
    power = models.CharField(max_length=50)
    boot_space = models.CharField(max_length=50)
    seating_capacity = models.IntegerField(default=5)
    max_torque = models.CharField(max_length=50)


class CarData(models.Model):
    carIDE = models.PositiveIntegerField(choices=IDE)
    caryear = models.IntegerField(
        default=datetime.datetime.now().year, choices=year)
    carbrand = models.ForeignKey(Carbrand, on_delete=models.CASCADE)
    carmodel = models.ForeignKey(Carmodel, on_delete=models.CASCADE)
    transmission = models.CharField(choices=trans, max_length=9, default="")
    kilometers = models.IntegerField(choices=KM, default=0)
    ownership = models.CharField(max_length=6, choices=owner, default='')
    fuletype = models.CharField(choices=fule, max_length=6, default="")
    price = models.PositiveIntegerField(default=0)
    city=models.CharField(default='',max_length=50)

class CarImage(models.Model):
    car = models.ForeignKey(CarData, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
