from django.urls import path
from .views import signup, verify_email, signin, get_details

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('verify-email/', verify_email, name='verify_email'),
    path('signin/', signin, name='signin'),
    path('get-details/', get_details, name='get_details'),
]