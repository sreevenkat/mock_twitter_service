"""tweets URL Configuration

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

from tweets import views as tweet_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', tweet_view.login_view, name='login_view'),
    url(r'^logout/$', tweet_view.logout_view, name='logout_view'),
    url(r'^tweets/$', tweet_view.get_all_tweets, name='get_all_tweets'),
    url(r'^tweet/(?P<pk>[0-9]+)/$', tweet_view.get_tweet, name='get_tweet'),
    url(r'^post-tweet/$', tweet_view.post_tweet, name='post_tweet'),
    url('', tweet_view.index, name='index'),
]
