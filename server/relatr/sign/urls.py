from django.conf.urls import url
from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token,
)

urlpatterns = [
    url(r'^obtain/', obtain_jwt_token),
    url(r'^verify/', verify_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
]
