# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import TutorialViewSet, DocumentViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'tutorials', TutorialViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)