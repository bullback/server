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


class NestedSpeechSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speech
        fields = ('head', 'body', 'path')


class NestedBubbleSerializer(serializers.ModelSerializer):
    speechs = NestedSpeechSerializer(many=True)

    class Meta:
        model = Bubble
        fields = ('head', 'body', 'trigger', 'speechs')


class NestedDocumentSerializer(serializers.ModelSerializer):
    bubbles = NestedBubbleSerializer(many=True)

    class Meta:
        model = Document
        fields = ('host', 'path', 'bubbles')


class NestedTutorialSerializer(serializers.ModelSerializer):
    documents = NestedDocumentSerializer(many=True)

    class Meta:
        model = Tutorial
        fields = ('head', 'body', 'documents')