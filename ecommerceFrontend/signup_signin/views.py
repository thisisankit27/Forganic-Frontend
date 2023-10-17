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
    
    return render(request, 'Authentication/verify_email.html')

# @method_decorator(csrf_exempt, name='dispatch')
# class SignupView(View):
#     def get(self, request):
#         return render(request, 'Authentication/signup.html')
    
#     def post(self, request):
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')
#         data = {
#             'first_name': first_name,
#             'last_name' : last_name,
#             'username': username,
#             'email': email,
#             'password': password,
#             'password2': password2
#         }
#         try:
#             response = requests.post('http://127.0.0.1:8000/Authentication/register/', data)
#             response.raise_for_status()  # Raise an exception for bad responses (4xx, 5xx)
#             context = {
#                 'response': response,
#                 'email': email
#             }
#             return redirect('VerifyEmail', context)
#         except requests.exceptions.RequestException:
#             messages.error(request, response)
#             return redirect('signup')

# @method_decorator(csrf_exempt, name='dispatch')        
# class VerifyEmailView(View):
#     def get(self, request):
#         return render(request, 'Authentication/verifyEmail.html')
#     def post(self, request):
#         email = request.POST.get('email')
#         try:
#             response = requests.post('http://127.0.0.1:8000/Authentication/verify-email/', {'email': email})
#             response.raise_for_status()
#             object = emailToken.objects.create(email=email, token=response.json().get('token'))
#             object.save()
#             return redirect('VerifyOtp', {'message': response})
#         except requests.exceptions.RequestException:
#             messages.error(request, response)
#             return redirect('VerifyEmail')

# @method_decorator(csrf_exempt, name='dispatch')     
# class VerifyOtpView(View):
#     def get(self, request):
#         return render(request, 'Authentication/verifyOtp.html')
#     def post(self, request):
#         otp = request.POST.get('otp')
#         email = request.POST.get('email')
#         data = {
#             'token': emailToken.objects.get(email=email).token,
#             'user_otp': otp
#         }
#         try:
#             response = requests.post('http://127.0.0.1:8000/Authentication/verify-email-otp/', data)
#             response.raise_for_status()
#             return redirect('login')
#         except requests.exceptions.RequestException:
#             messages.error(request, response)
#             return redirect('VerifyOtp')