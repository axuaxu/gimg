from django.conf.urls import patterns, include, url
from django.contrib import admin


import object_tools




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gimg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_img/', include(admin.site.urls)),

)
