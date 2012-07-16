"""
creating url for reg apps
"""


from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^logout/$','reg.views.do_logout'),
    url(r'^login/$', 'reg.views.do_login'),
    url(r'^/next=/$','reg.views.do_login'),
 
)   
