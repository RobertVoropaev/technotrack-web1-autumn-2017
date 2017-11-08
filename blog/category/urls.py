from django.conf.urls import url

from category.views import CategoryList, CategoryDetail, CategoryCreate, CategoryUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^all/$', CategoryList.as_view() , name="category_all"),
    url(r'^(?P<category_id>\d+)/$', CategoryDetail.as_view(), name="category_detail"),
    url(r'^create/$', login_required(CategoryCreate.as_view()), name="category_create"),
    url(r'^(?P<category_id>\d+)/update/$', login_required(CategoryUpdate.as_view()), name="category_update")
]
