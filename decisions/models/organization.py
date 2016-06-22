# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    label = models.CharField(max_length=255,
                             help_text=_("Post's label"))
    organization = models.ForeignKey('Organization')

    def __str__(self):
        return self.label


class Organization(models.Model):
    abstract = models.CharField(max_length=255, help_text=_('A one-line description of an organization'))

    def __str__(self):
        return self.abstract
