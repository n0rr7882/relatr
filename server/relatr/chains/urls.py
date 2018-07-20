from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as chain_views

chain_create_list = chain_views.CreateChainView.as_view()

chain_timeline_list = chain_views.TimelineChainView.as_view()

chain_detail = chain_views.DetailChainView.as_view()

like_create_delete = chain_views.ChainLikeView.as_view()

parent_chain_detail = chain_views.ParentChainView.as_view()

child_chain_list = chain_views.ChildChainView.as_view()


urlpatterns = format_suffix_patterns([
    url(
        r'^$',
        chain_create_list,
        name='chain_create_list'
    ),
    url(
        r'^timeline/$',
        chain_timeline_list,
        name='chain_timeline_list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        chain_detail,
        name='chain_detail'
    ),
    url(
        r'^(?P<pk>[0-9]+)/parent-chain/$',
        parent_chain_detail,
        name='parent_chain_detail'
    ),
    url(
        r'^(?P<pk>[0-9]+)/child-chains/$',
        child_chain_list,
        name='child_chain_list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/like/(?P<account_pk>[0-9]+)/$',
        like_create_delete,
        name='like_create_delete'
    ),
])
