from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account
from uuid import uuid4
from django.dispatch import receiver
from django.db.models import signals

import re


def chain_image_path(instance, filename):
    directory = instance.account.user.id
    name = uuid4()
    extension = filename.split('.')[-1]
    return 'users/{}/chains/{}.{}'.format(directory, name, extension)


class Chain(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='my_chains'
    )
    parent_chain = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='child_chains'
    )
    text = models.TextField(max_length=255)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=chain_image_path
    )
    tags = models.ManyToManyField(
        'Hashtag',
        null=True,
        blank=True,
        through='ChainTag',
        related_name='tagged_to',
        symmetrical=False
    )
    mentions = models.ManyToManyField(
        Account,
        null=True,
        blank=True,
        through='ChainMention',
        related_name='mentioned_to',
        symmetrical=False
    )
    likes = models.ManyToManyField(
        Account,
        null=True,
        blank=True,
        through='ChainLike',
        related_name='like_to',
        symmetrical=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'No.{}'.format(self.id)

    def save_tags(self):
        tags = re.findall(r'#(\w+)\b', self.text)
        
        for t in tags:
            tag, created = Hashtag.objects.get_or_create(name=t)
            relation, created = ChainTag.objects.get_or_create(
                chain=self,
                hashtag=tag
            )
            relation.save()

        return

    def get_tags(self):
        return self.tags.filter(included_tags__chain=self)

    def mention_to(self, target):
        mention, created = ChainMention.objects.get_or_create(
            chain=self,
            account=target
        )
        mention.save()

        return created

    def cancel_mention_to(self, target):
        mention, created = ChainMention.objects.get_or_create(
            chain=self,
            account=target
        )
        mention.delete()

        return not created

    def get_mentioned_accounts(self):
        return self.mentions.filter(mentioned_accounts__chain=self)

    def liked_from(self, account):
        like, created = ChainLike.objects.get_or_create(
            chain=self,
            account=account
        )
        like.save()

        return created

    def unliked_from(self, account):
        like, created = ChainLike.objects.get_or_create(
            chain=self,
            account=account
        )
        like.delete()

        return not created

    def get_liked_accounts(self):
        return self.likes.filter(liked_accounts__chain=self)

    def get_child_chains(self):
        return self.child_chains.all()

    class Meta:
        ordering = ('-created_at',)


class Hashtag(models.Model):
    name = models.CharField(max_length=144)

    def __str__(self):
        return self.name


class ChainTag(models.Model):
    chain = models.ForeignKey(
        Chain,
        on_delete=models.CASCADE,
        related_name='chains_tagged'
    )
    hashtag = models.ForeignKey(
        Hashtag,
        on_delete=models.CASCADE,
        related_name='included_tags'
    )

    def __str__(self):
        return '{} tagged in chain No.{}'.format(
            self.hashtag.name,
            self.chain.id
        )


class ChainMention(models.Model):
    chain = models.ForeignKey(
        Chain,
        on_delete=models.CASCADE,
        related_name='chains_mentioned'
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='mentioned_accounts'
    )
    mentioned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} mentioned in chain No.{}'.format(
            self.account.user.username,
            self.chain.id
        )

    class Meta:
        ordering = ('-mentioned_at',)


class ChainLike(models.Model):
    chain = models.ForeignKey(
        Chain,
        on_delete=models.CASCADE,
        related_name='chains_liked'
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='liked_accounts'
    )
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} liked chain No.{}'.format(
            self.account.user.username,
            self.chain.id
        )

    class Meta:
        ordering = ('-liked_at',)


@receiver(signals.post_save, sender=Chain)
def save_tags(sender, instance, **kwargs):
    instance.save_tags()
