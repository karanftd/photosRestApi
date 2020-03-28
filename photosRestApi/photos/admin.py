from django.contrib import admin
from photosRestApi.photos.models import Photo, Tag

# Register your models here.
admin.site.register(Photo)
admin.site.register(Tag)
