from django.conf.urls import patterns, include
from rest_framework import routers
from apps.apis.providerapi import views

router = routers.SimpleRouter()
router.register(r'provider', views.ProviderViewSet)

urlpatterns = patterns(
    '',
    (r'^', include(router.urls)),
    (r'^search$', views.SearchApi.as_view()),
    (r'^service/area/(?P<pk>[\w\d]+)/$', views.ServiceAreaApi.as_view()),
)
