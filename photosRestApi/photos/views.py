from django.shortcuts import render
from photosRestApi.photos.models import Photo
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
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
        
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Photo.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            user_obj = User.objects.get(username=user)
            queryset = queryset.filter(author_id=user_obj.id)
            
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset
