from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializer import SongsSerializer


# Create your views here.
class ListSongsView(generics.ListAPIView):
    """ provides a get method handler """

    queryset = Songs.objects.all()
    serializer_class = SongsSerializer