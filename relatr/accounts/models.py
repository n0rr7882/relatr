from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.db.models.signals import post_save


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
        User,
        blank=True,
        through='Follow',
        related_name='followers',
        symmetrical=False
    )

    def __str__(self):
        return self.user.username

    def follow_to(self, target):
        follow_info, created = Follow.objects.get_or_create(
            follower=self,
            following=target.user,
        )
        follow_info.save()
        return created

    def unfollow_to(self, target):
        follow_info, created = Follow.objects.get_or_create(
            follower=self,
            following=target.user,
        )
        follow_info.delete()
        return not created


class Follow(models.Model):
    follower = models.ForeignKey(Account, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} -> {}'.format(
            self.follower.user.username,
            self.following.username,
        )


def create_account(sender, **kwargs):
    if kwargs['created']:
        user_account = Account.objects.create(user=kwargs['instance'])

post_save.connect(create_account, sender=User)
