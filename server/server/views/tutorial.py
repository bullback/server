# -*- coding:utf-8 -*-

from rest_framework import viewsets
from rest_framework import permissions
from ..models import Tutorial, Document
from ..serializers import TutorialSerializer, DocumentSerializer


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
