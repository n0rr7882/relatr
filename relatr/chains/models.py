from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account
from uuid import uuid4
from django.dispatch import receiver
from django.db.models import signals


def chain_image_path(instance, filename):
    directory = instance.user.id
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
    mentions = models.ManyToManyField(
        Account,
        null=True,
        blank=True,
        through='ChainMention',
        related_name='mentioned_to',
        symmetrical=False
    )

    def __str__(self):
        return 'No.{}'.format(self.id)

    def add_tag(self, text):
        tag, created = ChainTag.objects.get_or_create(
            chain=self,
            tag=text
        )
        tag.save()

        return created

    def remove_tag(self, text):
        tag, created = ChainTag.objects.get_or_create(
            chain=self,
            tag=text
        )
        tag.delete()

        return not created

    def get_tags(self):
        return self.tags.all()

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
        return self.mentions.filter(mentioned_account__chain=self)


class ChainTag(models.Model):
    chain = models.ForeignKey(
        Chain,
        on_delete=models.CASCADE,
        related_name='tags'
    )
    tag = models.CharField(max_length=144)

    def __str__(self):
        return '"{}" in chain No.{}'.format(
            self.tag,
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
        related_name='mentioned_account'
    )
    mentioned_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} mentioned in chain No.{}'.format(
            self.account.user.username,
            self.chain.id
        )
