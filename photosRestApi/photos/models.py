import uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Photos(models.Model):
    STATE = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED'))
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    image = models.ImageField(upload_to='photo', blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    status = models.IntegerField(choices=STATE, default='0')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return '%s (author:%s)' % (
            self.caption,
            self.author.get_full_name()
        )

    def to_dict(self):
        ret = {
            'id': self.id,
            'image': self.image.url,
            'author': self.author.id,
            'content': self.caption,
        }
        return ret
