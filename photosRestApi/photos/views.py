from django.shortcuts import render
from photosRestApi.photos.models import Photos
from rest_framework import viewsets
from photosRestApi.photos.serializers import PhotosSerializer

# Create your views here.
class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
