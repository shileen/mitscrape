from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'websis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^scrape/', include('scrape.urls', namespace='scrape')),
    url(r'^admin/', include(admin.site.urls)),
]

if not settings.DEBUG:
    urlpatterns += url('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
