from django.conf.urls import url, include


urlpatterns = [
    url(r'^sign/', include('sign.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^users/', include('accounts.urls')),
    url(r'^chains/', include('chains.urls')),
]
