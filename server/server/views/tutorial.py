# -*- coding:utf-8 -*-

from rest_framework import viewsets
from rest_framework import permissions
from ..models import Tutorial
from ..serializers import TutorialSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.created_by = self.request.user
        obj.updated_by = self.request.user