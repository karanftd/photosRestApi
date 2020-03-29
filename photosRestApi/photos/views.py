from django.shortcuts import render
from photosRestApi.photos.models import Photo
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from photosRestApi.photos.serializers import PhotoSerializer

# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    """Handle CURD operation on Photos

    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    def destroy(self, request, *args, **kwargs):
        """Handle DELETE requests
        
        Arguments:
            request {Request} -- request object
        
        Returns:
            Response -- response to client
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        """Performe DELETE operations
        
        Arguments:
            instance {Photo} -- delete photo instance from records
        """
        instance.delete()
        
    def get_queryset(self):
        """
        Get request filtering for by User & State
        """
        queryset = Photo.objects.all().
        user = self.request.query_params.get('user', None)
        if user is not None:
            user_obj = User.objects.get(username=user)
            queryset = queryset.filter(author_id=user_obj.id)
            
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset
