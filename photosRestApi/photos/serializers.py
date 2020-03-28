from rest_framework import serializers
from photosRestApi.photos.models import Photo

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'author', 'caption', 'status')