from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


def thumbnail_path(instance, filename):
    directory = instance.user.username
    name = uuid4()
    extension = filename.split('.')[-1]
    return 'thumbnails/{}/{}.{}'.format(directory, name, extension)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True, upload_to=thumbnail_path)
    created_at = models.DateTimeField(auto_now=True)
    followings = models.ManyToManyField(
        'self',
        blank=True,
        related_name='followers',
        symmetrical=False
    )

    def __str__(self):
        return self.user.username
