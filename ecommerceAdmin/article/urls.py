from django.urls import path
from .views import article, articleDetail

urlpatterns = [
    path('article-list/', article, name='article'),
    path('article-detail/', articleDetail, name='articleDetail'),
]
