# -*- coding:utf-8 -*-

from django.db import models


class Tutorial(models.Model):
    class Meta:
        app_label = 'server'

    head = models.CharField(max_length=32)
    body = models.TextField()
    # TODO snapshot = models.ImageField(upload_to=)

    is_completed = models.BooleanField(default=False)

    created_by = models.ForeignKey('auth.User', related_name='tutorial_create_set')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey('auth.User', related_name='tutorial_update_set')
    updated_on = models.DateTimeField(auto_now=True)


class Document(models.Model):
    class Meta:
        app_label = 'server'


class Bubble(models.Model):
    class Meta:
        app_label = 'server'


class Offset(models.Model):
    class Meta:
        app_label = 'server'


class Target(models.Model):
    class Meta:
        app_label = 'server'


class Speech(models.Model):
    class Meta:
        app_label = 'server'