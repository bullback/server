# -*- coding:utf-8 -*-

from django.db import models


class Tutorial(models.Model):
    class Meta:
        app_label = 'server'

    title = models.CharField(max_length=32)
    description = models.TextField()
    # TODO snapshot = models.ImageField(upload_to=)

    is_completed = models.BooleanField(default=False)

    created_by = models.ForeignKey('auth.User', related_name='create_tutorials')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey('auth.User', related_name='update_tutorials')
    updated_on = models.DateTimeField(auto_now=True)


class Document(models.Model):
    class Meta:
        app_label = 'server'

    host = models.CharField(max_length=32)
    path = models.CharField(max_length=1024)
    # TODO snapshot = models.ImageField(upload_to=)

    tutorial = models.ForeignKey(Tutorial, related_name='documents')


class Bubble(models.Model):
    class Meta:
        app_label = 'server'

    TRIGGER_CHOICES = (
        ('N', 'N'),  # click next in speech
        ('C', 'C'),  # click button in html
    )

    title = models.CharField(max_length=32)
    description = models.TextField()

    trigger = models.CharField(max_length=8, choices=TRIGGER_CHOICES, default='N')

    is_init_tutorial = models.BooleanField(default=False)
    is_init_document = models.BooleanField(default=False)

    document = models.ForeignKey(Document, related_name='bubbles')


class Speech(models.Model):
    class Meta:
        app_label = 'server'

    title = models.CharField(max_length=32)
    description = models.TextField()
    path = models.TextField()

    bubble = models.ForeignKey(Bubble, related_name='speechs')