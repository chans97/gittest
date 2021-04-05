"""mydiary models for db"""
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Content(models.Model):
    title = models.CharField(max_length=10, blank=False)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default="")
    file = models.FileField(null=True)
