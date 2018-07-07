from django.contrib import admin
from .models import (
    Chain,
    ChainMention,
    ChainTag,
    ChainLike,
)

admin.site.register(Chain)
admin.site.register(ChainMention)
admin.site.register(ChainTag)
admin.site.register(ChainLike)
