from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('<slug>/',redirect_url,name='redirect_url')
]