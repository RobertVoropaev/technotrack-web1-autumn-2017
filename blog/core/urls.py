from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from core.views import UserList, UserDetail, UserUpdate;

urlpatterns = [
    url(r'^all/$', UserList.as_view(), name="user_all"),
    url(r'^(?P<user_id>\d+)/$', UserDetail.as_view(), name="user_detail"),
    url(r'^(?P<user_id>\d+)/update/$', login_required(UserUpdate.as_view()), name="user_update"),
]