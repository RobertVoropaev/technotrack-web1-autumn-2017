from django.conf.urls import url, include
from post.views import *;

urlpatterns = [
    url(r'^all/$', PostList.as_view() , name="post_all"),
    url(r'^(?P<post_id>\d+)/$', PostDetail.as_view(), name="post_id"),
]