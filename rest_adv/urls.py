from django.urls import path
from rest_adv import views

app_name = 'rest_adv'

urlpatterns = [
    path('', views.index, name='index'),
]