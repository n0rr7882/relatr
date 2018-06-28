from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.dispatch import receiver
from django.db.models import signals

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


def thumbnail_path(instance, filename):
    directory = instance.user.id
    name = uuid4()
    extension = filename.split('.')[-1]
    return 'users/{}/thumbnails/{}.{}'.format(directory, name, extension)


def banner_path(instance, filename):
    directory = instance.user.id
    name = uuid4()
    extension = filename.split('.')[-1]
    return 'users/{}/banners/{}.{}'.format(directory, name, extension)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thumbnail = ProcessedImageField(
        null=True,
        blank=True,
        upload_to=thumbnail_path,
        processors=[Thumbnail(300, 300)],
        options={'quality': 60},
        format='JPEG',
    )
    banner = models.ImageField(blank=True, upload_to=banner_path)
    created_at = models.DateTimeField(auto_now=True)
    follows = models.ManyToManyField(
        'self',
        null=True,
        blank=True,
        through='Follow',
        related_name='followed_to',
        symmetrical=False
    )

    def __str__(self):
        return self.user.username

    def follow_to(self, target):
        if self == target:
            return False

        follow_info, created = Follow.objects.get_or_create(
            follower=self,
            following=target,
        )
        follow_info.save()

        return created

    def unfollow_to(self, target):
        follow_info, created = Follow.objects.get_or_create(
            follower=self,
            following=target,
        )
        follow_info.delete()

        return not created

    def get_followings(self):
        return self.follows.filter(followings__follower=self)

    def get_followers(self):
        return self.followed_to.filter(followers__following=self)


class Follow(models.Model):
    follower = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='followers'
    )
    following = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='followings'
    )
    followed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} -> {}'.format(
            self.follower.user.username,
            self.following.user.username,
        )


@receiver(signals.post_save, sender=User)
def create_account(sender, instance, **kwargs):
    if kwargs['created']:
        Account.objects.create(user=instance)


@receiver(signals.post_delete, sender=Account)
def delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()
