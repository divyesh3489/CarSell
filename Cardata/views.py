from django.shortcuts import render, redirect
from .forms import Add_Car
from .models import Carmodel, CarImage, CarData, Carbrand
from django.views.generic.edit import CreateView
from django.http import JsonResponse
import pickle
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.


def index(request):
    cars = CarData.objects.all()
    return render(request, 'Cardata/index.html', {'cars': cars})


@login_required
def carform(request):
    form = Add_Car()
    if request.method == 'POST':
        form = Add_Car(request.POST, request.FILES)
        form.instance.username = request.user
        print(form.instance.username)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            car = form.save()
            for image in request.FILES.getlist('images'):
                CarImage.objects.create(car=car, image=image)
            return redirect("Cardata:index")
        else:
            print(form.errors)
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


def car_detalis(reuqest, pk):
    cars = CarData.objects.get(pk=pk)
    return render(reuqest, 'Cardata/details.html', {'cars': cars})


def cardata(request):
    cars = CarData.objects.all()
    carbarnds = Carbrand.objects.all()
    show_button = True
    print(request.GET.getlist('carbrand'))
    if request.GET.getlist('carbrand') or (request.GET.get('max') and request.GET.get('min')) or request.GET.get('city'):
        cars = CarData.objects.filter(
            carbrand__in=request.GET.getlist('carbrand')) & (CarData.objects.filter(price__gt=request.GET.get('min')) & CarData.objects.filter(price__lt=request.GET.get('max'))) & CarData.objects.filter(city=request.GET.get('city'))
        if not request.GET.getlist('carbrand') and not request.GET.get('city'):
            cars = CarData.objects.filter(price__gt=request.GET.get('min')) & CarData.objects.filter(price__lt=request.GET.get('max'))
        if not request.GET.getlist('carbrand'):
            cars = CarData.objects.filter(price__gt=request.GET.get(
                'min')) & CarData.objects.filter(price__lt=request.GET.get('max')) & CarData.objects.filter(city=request.GET.get('city'))
        if not request.GET.get('city'):
            cars = CarData.objects.filter(
                carbrand__in=request.GET.getlist('carbrand')) & (CarData.objects.filter(price__gt=request.GET.get('min')) & CarData.objects.filter(price__lt=request.GET.get('max')))
    return render(request, 'Cardata/filter.html', {'cars': cars, 'show_button': show_button, "carbrand": carbarnds})
