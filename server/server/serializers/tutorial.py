# -*- coding:utf-8 -*-

from rest_framework import serializers
from ..models import Tutorial, Document, Bubble, Speech


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(many=True, view_name='document-detail')

    class Meta:
        model = Tutorial
        fields = ('url', 'head', 'body', 'documents')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    bubbles = serializers.HyperlinkedRelatedField(many=True, view_name='bubble-detail')

    class Meta:
        model = Document
        fields = ('url', 'host', 'path', 'bubbles', 'tutorial')


class BubbleSerializer(serializers.HyperlinkedModelSerializer):
    speechs = serializers.HyperlinkedRelatedField(many=True, view_name='speech-detail')

    class Meta:
        model = Bubble
        fields = ('url', 'head', 'body', 'trigger', 'speechs', 'document')


class SpeechSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Speech
        fields = ('url', 'head', 'body', 'path', 'bubble')