from rest_framework import serializers
from photosRestApi.photos.models import Photos

class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photos
        fields = ('id', 'image', 'author', 'caption', 'status')