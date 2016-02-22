from django.conf.urls import patterns, include, url
from apps.apis import urls as apis_urls

urlpatterns = patterns(
    '',
    # API Urls
    url(r'^api/', include(apis_urls)),
)
