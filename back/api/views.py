from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import SalarieSerializer
from api.models import Salarie
# Create your views here.

class SalarieViewset(viewsets.ModelViewSet):
    queryset = Salarie.objects.all()
    serializer_class = SalarieSerializer