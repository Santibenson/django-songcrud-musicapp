from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from . models import *
from . serializers import *

class ArtisteViewSet(viewsets.ModelViewSet):
     queryset = Artiste.objects.all()
     serializer_class = ArtisteSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer