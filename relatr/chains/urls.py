from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as chain_views

chain_create_list = chain_views.CreateChainView.as_view()

chain_detail = chain_views.DetailChainView.as_view()

tag_create_delete = chain_views.ChainTagView.as_view()

mention_create_delete = chain_views.ChainMentionView.as_view()

like_create_delete = chain_views.ChainLikeView.as_view()


urlpatterns = format_suffix_patterns([
    url(
        r'^$',
        chain_create_list,
        name='chain_create_list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        chain_detail,
        name='chain_detail'
    ),
    url(
        r'^(?P<pk>[0-9]+)/tag/(?P<tag_text>[^\s]+)/$',
        tag_create_delete,
        name='tag_create_delete'
    ),
    url(
        r'^(?P<pk>[0-9]+)/mention/(?P<account_pk>[0-9]+)/$',
        mention_create_delete,
        name='mention_create_delete'
    ),
    url(
        r'^(?P<pk>[0-9]+)/like/(?P<account_pk>[0-9]+)/$',
        like_create_delete,
        name='like_create_delete'
    ),
])
