from django.conf.urls import url
from core.views import *;

urlpatterns = [
    url(r'^all/$', UserList.as_view(), name="user_all"),
    url(r'^(?P<user_id>\d+)/$', UserDetail.as_view(), name="user_id"),
]