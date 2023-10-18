from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import emailToken

# Create your views here.
import requests

def signup(request):
    return render(request, 'Authentication/signup.html')

def verify_email(request):
    email = request.GET.get('email')
    context = {
        'email': email
    }
    return render(request, 'Authentication/verify_email.html', context)

def signin(request):
    return render(request, 'Authentication/signin.html')

def get_details(request):
    return render(request, 'Authentication/get-details.html')

def forget_password(request):
    return render(request, 'Authentication/forget-password.html')