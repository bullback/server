# -*- coding:utf-8 -*-

from rest_framework import serializers
from ..models import Tutorial, Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ('url', 'host', 'path', 'tutorial')


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    document_set = DocumentSerializer(many=True)

    class Meta:
        model = Tutorial
        fields = ('url', 'head', 'body', 'document_set')