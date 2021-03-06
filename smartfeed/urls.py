from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [ 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^smartfeed/', include('smartfeed.apps.feedredirector.urls', namespace='smartfeed')),
]

# Development
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = media + staticfiles_urlpatterns() + urlpatterns
