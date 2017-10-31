"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import *;
from post.views import *;
from category.views import *;

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', show_main, name="main_page"),

    url(r'^user/all/$', show_user_all, name="user_all"),
    url(r'^user/(?P<user_id>\d+)/$', show_user_id, name="user_id"),

    url(r'^post/all/$', show_post_all, name="post_all"),
    url(r'^post/(?P<post_id>\d+)/$', show_post_id, name="post_id"),

    url(r'^category/all/$', show_category_all, name="category_all"),
    url(r'^category/(?P<category_id>\d+)/$', show_category_id, name="category_id"),

]
