from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as chain_views

chain_create_list = chain_views.CreateChainView.as_view()


urlpatterns = format_suffix_patterns([
    url(
        r'^$',
        chain_create_list,
        name='chain_create_list'
    ),
])
