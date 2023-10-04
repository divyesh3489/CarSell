from django.shortcuts import render, redirect, get_object_or_404
from .form import Registration, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import EmailVerificationToken, CustomUser
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Registration(request.POST)
            if form.is_valid():
                form.save()
                newuser = form.cleaned_data['email']
                newuser = CustomUser.objects.get(email=newuser)
                token = default_token_generator.make_token(newuser)
                EmailVerificationToken.objects.create(
                    user=newuser, token=token)
                user_ip = get_client_ip(request)
                verification_link = f"http://{user_ip}:8000/user/verify-email/{token}/"
                subject = "Email Verification"
                message = f"Click the following link to verify your email: {verification_link}"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [newuser.email]
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Verify your email')
                return redirect('user:login')
        else:
            form = Registration()
        return render(request, 'user/Signup.html', {'form': form})
    else:
        return redirect("Cardata:index")


def EmailVerification(request, token):
    token_obj = get_object_or_404(EmailVerificationToken, token=token)
    print(token_obj.user)
    if default_token_generator.check_token(token_obj.user, token):
        token_obj.user.is_active = True
        token_obj.user.save()
        token_obj.delete()
        return render(request, 'user/verification.html', {"messages": "Email successfully verified."})
    return render(request, 'user/verification.html', {"messages": "Email is alredy Verifed"})


def LoginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            print(form.is_valid())
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("Cardata:index")
        else:
            form = LoginForm()
        newuser=request.POST.get('username')
        error=''
        if newuser:
            if CustomUser.objects.get(email=newuser):
                error="Verify your email"
        return render(request, 'user/login.html', {'form': form,'error':error})
    return redirect('Cardata:index')


def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('user:login')
    else:
        return redirect('user:login')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
