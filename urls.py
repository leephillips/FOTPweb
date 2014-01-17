from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^admin/start/$', 'ap.boarddocs.views.start'), 
     (r'^admin/directory/$', 'ap.boarddocs.views.directory'), 
     (r'^admin/minutes/$', 'ap.boarddocs.views.minutetop'), 
     (r'^admin/otherfiles/$', 'ap.boarddocs.views.otherfilestop'), 
     (r'^admin/budget/$', 'ap.boarddocs.views.budgettop'), 
     (r'^admin/agenda/$', 'ap.boarddocs.views.agendatop'), 
     (r'^admin/legal/$', 'ap.boarddocs.views.legaltop'), 
     (r'^admin/history/$', 'ap.boarddocs.views.historicaltop'), 
     (r'^admin/otherfiles/$', 'ap.boarddocs.views.otherfilestop'), 
     (r'^admin/pictures/$', 'ap.boarddocs.views.gallery'), 
     url(r'^admin/', include(admin.site.urls)),
     (r'^bio/(.*)/$', 'ap.apdirposts.views.bio'),
     (r'^post/(.*)/$', 'ap.apdirposts.views.post'),
     (r'^event/(.*)/$', 'ap.apdirposts.views.event'),
     (r'^join/$', 'ap.apdirposts.views.join'),
     (r'^donate/$', 'ap.apdirposts.views.donate'),
     (r'^about/$', 'ap.apdirposts.views.about'),
     (r'^about-us/$', 'ap.apdirposts.views.post', {'which': '7'}),
     (r'^history/$', 'ap.apdirposts.views.post', {'which': '9'}),
     (r'^photos/$', 'ap.apdirposts.views.post', {'which': '10'}),
     (r'^movies/$', 'ap.apdirposts.views.movies'),
     (r'^starchart/$', 'ap.apdirposts.views.starchart'),
     (r'^notice/(.*)/$', 'ap.apdirposts.views.notice'),
     (r'^post/$', 'ap.apdirposts.views.posttop'),
     (r'^notice/$', 'ap.apdirposts.views.noticetop'),
     (r'^event/$', 'ap.apdirposts.views.eventtop'),
     (r'^corner/$', 'ap.apdirposts.views.posttop'),
     (r'^science/$', 'ap.apdirposts.views.posttop'),
     (r'^website/$', 'ap.apdirposts.views.website'),
     (r'^$', 'ap.apdirposts.views.front'),
)
