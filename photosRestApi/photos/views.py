from django.shortcuts import render
from photosRestApi.photos.models import Photo
from rest_framework import viewsets
from rest_framework.response import Response
from photosRestApi.photos.serializers import PhotoSerializer

# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()
