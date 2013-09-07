from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     (r'^bio/(.*)/$', 'ap.apdirposts.views.bio'),
     (r'^post/(.*)/$', 'ap.apdirposts.views.post'),
     (r'^event/(.*)/$', 'ap.apdirposts.views.event'),
     (r'^notice/(.*)/$', 'ap.apdirposts.views.notice'),
     (r'^post/$', 'ap.apdirposts.views.posttop'),
     (r'^notice/$', 'ap.apdirposts.views.noticetop'),
     (r'^event/$', 'ap.apdirposts.views.eventtop'),
     (r'^$', 'ap.apdirposts.views.front'),
)
