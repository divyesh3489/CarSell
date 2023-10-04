from django.shortcuts import render
from .forms import Add_Car
from .models import Carmodel, CarImage,CarData
from django.http import JsonResponse
import pickle
import datetime
# Create your views here.

def index(request):
    cars = CarData.objects.all()
    return render(request, 'Cardata/index.html', {'cars': cars})

def carform(request):
    form = Add_Car()
    if request.method == 'POST':
        form = Add_Car(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            car = form.save()
            for image in request.FILES.getlist('images'):
                print(image)
                CarImage.objects.create(car=car, image=image)
            return render(request, 'Cardata/index.html')
        else:
            for image in request.FILES.getlist('images'):
                print(image)
            print("form is not valid")
    return render(request, 'Cardata/carform.html', {'form': form})


def load_models(request):
    carbrand_id = request.GET.get('carbarnd_id')
    models = Carmodel.objects.filter(carbrand=carbrand_id)
    return JsonResponse(list(models.values('id', 'carmodel')), safe=False)


def get_price(request):
    d_owner = {'1st': 0, '2nd': 1, '3rd': 1, 'dealer': 0}
    caride = int(request.GET.get('caride'))//100000
    carkm = int(request.GET.get('carkm'))
    carowner = request.GET.get('carowner')
    carfule = request.GET.get('carfule')
    cartrans = request.GET.get('cartrans')
    owner = d_owner[carowner]

    caryear = datetime.datetime.now().year-int(request.GET.get('caryear'))
    print(caride, carkm, carfule, cartrans, carowner, owner, caryear)
    if (carowner == '1st' or carowner == '2nd' or carowner == '3rd'):
        carowner = 0
    else:
        carowner = 1
    if (carfule == 'Petrol'):
        petrol = 1
        diesel = 0
    elif (carfule == 'CNG'):
        petrol = 0
        diesel = 0
    else:
        petrol = 0
        diesel = 1
    if (cartrans == 'Manual'):
        cartrans = 1
    else:
        cartrans = 0
    print(caride, carkm, owner, caryear, diesel, petrol, carowner, cartrans)
    lr = pickle.load(
        open("D:\python\django\CarSite\CarSell\Cardata\CarModel.pkl", "rb"))
    data = round(lr.predict(
        [[caride, carkm, owner, caryear, diesel, petrol, carowner, cartrans]])[0], 2)
    # data=lr.predict([[6.0,120000,0,6,0,1,1,0]])
    data = [data]
    print(data)
    return JsonResponse(list(data), safe=False)

def car_detalis(reuqest,pk):
    cars=CarData.objects.get(pk=pk)
    return render(reuqest,'Cardata/details.html',{'cars':cars})
