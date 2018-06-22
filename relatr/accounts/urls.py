from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as account_views

user_list = account_views.CreateUserView.as_view()

user_detail = account_views.DetailUserView.as_view()

account_list = account_views.AccountView.as_view({
    'get': 'list',
    'post': 'create',
})

account_detail = account_views.AccountView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = format_suffix_patterns([
    url(r'^users/$', user_list, name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user_detail'),
    url(r'^accounts/$', account_list, name='account_list'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', account_detail, name='account_detail'),
    url(r'^change-password/$', account_views.UpdatePasswordView.as_view()),
])
