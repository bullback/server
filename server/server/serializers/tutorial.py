# -*- coding:utf-8 -*-

from rest_framework import serializers
from ..models import Tutorial, Document, Bubble


class BubbleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bubble
        fields = ('url', 'head', 'body', 'trigger', 'document')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    bubbles = serializers.HyperlinkedRelatedField(many=True, view_name='bubble-detail')

    class Meta:
        model = Document
        fields = ('url', 'host', 'path', 'bubbles', 'tutorial')


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(many=True, view_name='document-detail')

    class Meta:
        model = Tutorial
        fields = ('url', 'head', 'body', 'documents')