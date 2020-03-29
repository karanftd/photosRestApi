import uuid
import re
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from photosRestApi.photos.storage_backends import PublicMediaStorage


def get_file_path(instance, filename):
    """generate unique file name for image
    
    Arguments:
        instance {Photo} -- Photo instance
        filename {str} -- file name
    
    Returns:
        str -- filename
    """
    ext = filename.split('.')[-1]
    return "%s.%s" % (uuid.uuid4(), ext)

@receiver(pre_save)
def my_callback(sender, instance, *args, **kwargs):
    """before saving update the tags
    
    Arguments:
        sender -- [description]
        instance {Photo} -- Photo instance
    """
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
    """Tags model, store tag information
    
    """
    tag = models.CharField(max_length=100)


# Create your models here.
class Photo(models.Model):
    """Photo model, used to store photo information
    
    image(required): store the image to S3
    author(required): user who uploads the image
    caption(optional): description about the image including tags
    status(optional, default=DRAFT): state of image
    created_at:
    published_at: datetime when published at
    tags: contains tag
    
    """
    STATE = (
    ('DRAFT', 'DRAFT'),
    ('PUBLISHED', 'PUBLISHED'))
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    image = models.ImageField(storage=PublicMediaStorage(), upload_to=get_file_path, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    status = models.TextField(choices=STATE, default='DRAFT')
    created = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)
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
