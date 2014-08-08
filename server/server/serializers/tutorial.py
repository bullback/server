# -*- coding:utf-8 -*-

from rest_framework import serializers
from ..models import Tutorial, Feedback, Document, Bubble, Speech, Comment


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(many=True, view_name='document-detail')

    class Meta:
        model = Tutorial
        fields = ('url', 'title', 'description', 'documents')


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ('content', 'created_by', 'created_on')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    bubbles = serializers.HyperlinkedRelatedField(many=True, view_name='bubble-detail')

    class Meta:
        model = Document
        fields = ('url', 'host', 'path', 'bubbles', 'tutorial')


class BubbleSerializer(serializers.HyperlinkedModelSerializer):
    speechs = serializers.HyperlinkedRelatedField(many=True, view_name='speech-detail')

    class Meta:
        model = Bubble
        fields = ('url', 'title', 'description', 'trigger', 'speechs', 'prev', 'document')


class SpeechSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Speech
        fields = ('url', 'title', 'description', 'path', 'bubble')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'created_by', 'created_on')


class NestedSpeechSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speech
        fields = ('title', 'description', 'path')


class NestedBubbleSerializer(serializers.ModelSerializer):
    speechs = NestedSpeechSerializer(many=True)

    class Meta:
        model = Bubble
        fields = ('title', 'description', 'trigger', 'speechs', 'prev')


class NestedDocumentSerializer(serializers.ModelSerializer):
    bubbles = NestedBubbleSerializer(many=True)

    class Meta:
        model = Document
        fields = ('host', 'path', 'bubbles')


class NestedTutorialSerializer(serializers.ModelSerializer):
    documents = NestedDocumentSerializer(many=True)

    class Meta:
        model = Tutorial
        fields = ('title', 'description', 'documents')