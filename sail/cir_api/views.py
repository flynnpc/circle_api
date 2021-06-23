from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CircleSerializer
from .models import Circle

# Create your views here.
class CircleViewSet(viewsets.ModelViewSet):
    queryset = Circle.objects.all().order_by('id')
    serializer_class = CircleSerializer
