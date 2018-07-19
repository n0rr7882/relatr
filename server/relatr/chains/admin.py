from django.contrib import admin
from .models import (
    Chain,
    Hashtag,
    ChainTag,
    ChainLike,
    ChainMention,
)

admin.site.register(Chain)
admin.site.register(Hashtag)
admin.site.register(ChainTag)
admin.site.register(ChainLike)
admin.site.register(ChainMention)
