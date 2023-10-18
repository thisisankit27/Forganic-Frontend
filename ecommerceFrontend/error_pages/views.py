# your_app/views.py
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'Error/404.html', status=404)
