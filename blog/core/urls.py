from django.conf.urls import url

from core.views import UserList, UserDetail, UserUpdate, UserChangePassword;

urlpatterns = [
    url(r'^all/$', UserList.as_view(), name="user_all"),
    url(r'^(?P<user_id>\d+)/$', UserDetail.as_view(), name="user_detail"),
    url(r'^(?P<user_id>\d+)/update/$', UserUpdate.as_view(), name="user_update"),
    url(r'^(?P<user_id>\d+)/change_password/$', UserChangePassword.as_view(), name="user_change_password")
]