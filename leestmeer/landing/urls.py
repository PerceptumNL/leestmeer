from django.conf.urls import patterns, include, url
from django.contrib import admin
# Examples:
# url(r'^$', 'leestmeer.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = patterns('',
    url(r'^$', 'landing.views.home', name='home'),

)
