from django.shortcuts import render, HttpResponse

from rest_framework import viewsets
from .serializers import PrimeSerializer
from .models import Prime

# Create your views here.

def health(req):
    return HttpResponse('{status:"ok"}')


class PrimesViewSet(viewsets.ModelViewSet):
    serializer_class = PrimeSerializer
    queryset = Prime.objects.all().order_by("number")