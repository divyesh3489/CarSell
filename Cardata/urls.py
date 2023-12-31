from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Cardata'
urlpatterns = [
    path('carform/',views.carform,name='carform'),
    path('cardata/',views.cardata,name='cardata'),
    path('',views.index,name='index'),
    path('ajax/load-model',views.load_models,name='ajax_load_model'),
    path('ajax/get-price',views.get_price,name='ajax_price_url'),
    path('detail/<int:pk>',views.car_detalis,name='details')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)