from django.conf.urls import url, include

from post.views import PostList, PostDetail, PostCreate, PostUpdate;
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^all/$', PostList.as_view() , name="post_all"),
    url(r'^(?P<post_id>\d+)/$', PostDetail.as_view(), name="post_detail"),
    url(r'^create/$', login_required(PostCreate.as_view()) , name="post_create"),
    url(r'^(?P<post_id>\d+)/update/$', login_required(PostUpdate.as_view()) , name="post_update"),
    url(r'^(?P<post_id>\d+)/change_password/$', login_required(PostUpdate.as_view()) , name="post_update")
]