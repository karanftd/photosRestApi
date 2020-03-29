from rest_framework import serializers
from photosRestApi.photos.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    """serializer for Photo

    """
    class Meta:
        model = Photo
        fields = ('id', 'image', 'author', 'caption', 'status', 'published_at')