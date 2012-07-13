"""
This code should be copy and pasted into blog/urls.py
"""


from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'post.views.home'),
    url(r'^posts/$', 'post.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'post.views.post_detail',name='post_detail'),
    url(r'^posts/search/(?P<term>\w+)/$','post.views.post_search'),
    url(r'^posts/edit_comment/(?P<id>\d+)/edit/$','post.views.edit_comment',name='edit_comment'),
)   
