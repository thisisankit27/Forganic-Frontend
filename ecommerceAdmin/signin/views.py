from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request, 'Auth/signin.html')