from django.conf.urls import url, include

from post.views import PostList, PostCreate, PostUpdate, PostDetailAndCommentCreate;
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^all/$', PostList.as_view() , name="post_all"),
    url(r'^(?P<post_id>\d+)/$', PostDetailAndCommentCreate.as_view(), name="post_detail"),
    url(r'^create/$', login_required(PostCreate.as_view()) , name="post_create"),
    url(r'^(?P<post_id>\d+)/update/$', login_required(PostUpdate.as_view()) , name="post_update"),
]