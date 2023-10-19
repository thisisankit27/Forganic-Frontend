from django.urls import path
from .views import item, itemDetail, itemPOST

urlpatterns = [
    path('item/', item, name='item'),
    path('itemDetail/', itemDetail, name='itemDetail'),
    path('itemPOST/', itemPOST, name='itemPOST'),
]