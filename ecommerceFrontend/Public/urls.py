from django.urls import path
from .views import homepage, item

urlpatterns = [
    path('home/', homepage, name='homepage'),
    path('item/', item, name='item'),
]