import uuid
from django.contrib.auth.models import User
from django.db import models
from photosRestApi.photos.storage_backends import PublicMediaStorage


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    return "%s.%s" % (uuid.uuid4(), ext)

# Create your models here.
class Photo(models.Model):
    STATE = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED'))
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    image = models.ImageField(storage=PublicMediaStorage(), upload_to=get_file_path, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    status = models.IntegerField(choices=STATE, default='0')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return '%s (author:%s)' % (
            self.caption,
            self.author.username
        )

    def to_dict(self):
        ret = {
            'id': self.id,
            'image': self.image.url,
            'author': self.author.id,
            'content': self.caption,
        }
        return ret
