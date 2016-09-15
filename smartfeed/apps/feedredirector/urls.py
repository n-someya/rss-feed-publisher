from django.conf.urls import url
from smartfeed.apps.feedredirector import views

urlpatterns = [
        url(r'^feed/(?P<article_id>\d+)/(?P<user_id>\d+)/$', views.show, name='show'),
        ]

