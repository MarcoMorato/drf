from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import WomenSerializer


class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
