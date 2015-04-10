from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

# Examples:
# url(r'^$', 'leestmeer.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = patterns('',
    (r'^$', include('landing.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/',  include(admin.site.urls)), # admin site
    ('^markdown/', include( 'django_markdown.urls')),
)
