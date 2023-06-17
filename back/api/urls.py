from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import SalarieViewset

salarie = DefaultRouter()
salarie.register('salarie', SalarieViewset, basename= 'Salarie')
urlpatterns = [
    path('', include(salarie.urls)),
]