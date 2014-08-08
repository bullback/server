# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import TutorialViewSet, FeedbackViewSet, DocumentViewSet, BubbleViewSet, SpeechViewSet, CommentViewSet, \
    NestedTutorialViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'nested-tutorials', NestedTutorialViewSet)
router.register(r'tutorials', TutorialViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'bubbles', BubbleViewSet)
router.register(r'speechs', SpeechViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)