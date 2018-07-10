from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as account_views

user_create_list = account_views.CreateUserView.as_view()

user_detail = account_views.DetailUserView.as_view()

account_list = account_views.ListAccountView.as_view()

account_detail = account_views.DetailAccountView.as_view()

account_followings = account_views.AccountFollowingsView.as_view()

account_followers = account_views.AccountFollowersView.as_view()

change_password = account_views.ChangePasswordView.as_view()


urlpatterns = format_suffix_patterns([
    url(
        r'^$',
        user_create_list,
        name='user_create_list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        user_detail,
        name='user_detail'
    ),
    url(
        r'^(?P<pk>[0-9]+)/follow/$',
        account_views.FollowView.as_view(),
        name='follow'
    ),
    url(
        r'^accounts/$',
        account_list,
        name='account_list'
    ),
    url(
        r'^accounts/(?P<pk>[0-9]+)/$',
        account_detail,
        name='account_detail'
    ),
    url(
        r'^accounts/(?P<pk>[0-9]+)/followings/$',
        account_followings,
        name='account_followings'
    ),
    url(
        r'^accounts/(?P<pk>[0-9]+)/followers/$',
        account_followers,
        name='account_followers'
    ),
    url(
        r'^change-password/$',
        change_password,
        name='change_password'
    ),
])
