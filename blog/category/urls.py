from django.conf.urls import url, include
from category.views import *;

urlpatterns = [
    url(r'all/$', CategoryList.as_view() , name="category_all"),
    url(r'(?P<category_id>\d+)/$', CategoryDetail.as_view(), name="category_id"),
]
