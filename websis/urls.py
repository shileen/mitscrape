from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'websis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^scrape/', include('scrape.urls', namespace='scrape')),
    url(r'^admin/', include(admin.site.urls)),
]
