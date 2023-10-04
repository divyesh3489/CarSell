from django.contrib import admin
from .models import CustomUser,EmailVerificationToken
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(EmailVerificationToken)