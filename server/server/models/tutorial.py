# -*- coding:utf-8 -*-

from django.db import models


class Tutorial(models.Model):
    class Meta:
        app_label = 'server'


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