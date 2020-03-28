import uuid
import re
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from photosRestApi.photos.storage_backends import PublicMediaStorage


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    return "%s.%s" % (uuid.uuid4(), ext)

@receiver(pre_save)
def my_callback(sender, instance, *args, **kwargs):
    if not isinstance(instance, Photo):
        return

    tags = re.findall(r"#(\w+)", instance.caption)
    print(tags)
    tags_objs = []
    for tag in tags:
        obj, _ = Tag.objects.get_or_create(tag=tag)
        tags_objs.append(obj)        
    
    instance.tags.set(tags_objs)


class Tag(models.Model):
    tag = models.CharField(max_length=100)


# Create your models here.
class Photo(models.Model):
    STATE = (
    ('DRAFT', 'DRAFT'),
    ('PUBLISHED', 'PUBLISHED'))
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    image = models.ImageField(storage=PublicMediaStorage(), upload_to=get_file_path, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    status = models.TextField(choices=STATE, default='0')
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
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
