from django.shortcuts import render
from photosRestApi.photos.models import Photo
from rest_framework import viewsets
from photosRestApi.photos.serializers import PhotoSerializer

# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
