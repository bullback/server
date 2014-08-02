# -*- coding:utf-8 -*-

from rest_framework import viewsets
from rest_framework import permissions
from ..models import Tutorial, Document, Bubble
from ..serializers import TutorialSerializer, DocumentSerializer, BubbleSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.created_by = self.request.user
        obj.updated_by = self.request.user


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BubbleViewSet(viewsets.ModelViewSet):
    queryset = Bubble.objects.all()
    serializer_class = BubbleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)