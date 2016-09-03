from django.conf.urls import patterns, include, url
from django.contrib import admin
from apdirposts.views import smile

admin.autodiscover()

urlpatterns = patterns('',
     (r'^admin/', include(admin.site.urls)),
     (r'^admin/start/$', 'ap.boarddocs.views.start'), 
     # (r'^admin/todo/$', 'ap.boarddocs.views.todo'), 
     (r'^admin/directory/$', 'ap.boarddocs.views.directory'), 
     (r'^admin/minutes/$', 'ap.boarddocs.views.minutetop'), 
     (r'^admin/otherfiles/$', 'ap.boarddocs.views.otherfilestop'), 
     (r'^admin/budget/$', 'ap.boarddocs.views.budgettop'), 
     (r'^admin/agenda/$', 'ap.boarddocs.views.agendatop'), 
     (r'^admin/legal/$', 'ap.boarddocs.views.legaltop'), 
     (r'^admin/history/$', 'ap.boarddocs.views.historicaltop'), 
     (r'^admin/otherfiles/$', 'ap.boarddocs.views.otherfilestop'), 
     (r'^admin/pictures/$', 'ap.boarddocs.views.gallery'), 
     # (r'^todo/', include('todo.urls')),
     (r'^smile/$', smile),
     (r'^bio/(.*)/$', 'ap.apdirposts.views.bio'),
     (r'^setdonation', 'ap.apdirposts.views.setdonation'),
     (r'^post/preview/(.*)/$', 'ap.apdirposts.views.preview_post'),
     (r'^post/(.*)/$', 'ap.apdirposts.views.post'),
     (r'^event/(.*)/$', 'ap.apdirposts.views.event'),
     (r'^community_event/(.*)/$', 'ap.apdirposts.views.community_event'),
     (r'^join/$', 'ap.apdirposts.views.join'),
     (r'^sf2016/$', 'ap.apdirposts.views.sf2016'),
     (r'^planets/$', 'ap.apdirposts.views.planets'),
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
     (r'^newarticle/$', 'ap.apdirposts.views.newarticle'),
     (r'^newarticle/(.*)/$', 'ap.apdirposts.views.newarticle'),
     (r'^aps_banner/$', 'ap.apdirposts.views.aps_banner'),
     (r'^tinymce/', include('tinymce.urls')),
     (r'^$', 'ap.apdirposts.views.front'),
     (r'^x7297/$', 'ap.apdirposts.views.x7297'),
     (r'^preview/$', 'ap.apdirposts.views.preview_front'),
     (r'^configure_slideshow/$', 'ap.apdirposts.views.configure_slideshow'),
)
