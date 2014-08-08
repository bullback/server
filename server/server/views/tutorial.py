# -*- coding:utf-8 -*-

from rest_framework import viewsets
from rest_framework import permissions
from ..models import Tutorial, Feedback, Document, Bubble, Speech, Comment
from ..serializers import TutorialSerializer, FeedbackSerializer, DocumentSerializer, BubbleSerializer, \
    SpeechSerializer, CommentSerializer, NestedTutorialSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.created_by = self.request.user
        obj.updated_by = self.request.user


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BubbleViewSet(viewsets.ModelViewSet):
    queryset = Bubble.objects.all()
    serializer_class = BubbleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SpeechViewSet(viewsets.ModelViewSet):
    queryset = Speech.objects.all()
    serializer_class = SpeechSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class NestedTutorialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = NestedTutorialSerializer