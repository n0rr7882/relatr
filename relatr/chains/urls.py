from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as chain_views

chain_create_list = chain_views.CreateChainView.as_view()

chain_detail = chain_views.DetailChainView.as_view()

tag_create_list = chain_views.CreateTagView.as_view()

tag_detail = chain_views.DetailTagView.as_view()


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
        r'^(?P<pk>[0-9]+)/tags/$',
        tag_create_list,
        name='tag_create_list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/tags/(?P<tag>[^\s]+)/$',
        tag_detail,
        name='tag_detail'
    )
])
