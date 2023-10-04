from django.urls import path, include
from .views import register, LoginView, Logout,EmailVerification


app_name = 'user'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', Logout, name='logout'),
    path('verify-email/<str:token>/',EmailVerification, name='verify_email'),
]
