# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .organization import Post  # noqa
from .organization import Organization  # noqa


class Membership(models.Model):
    person = models.ForeignKey('Person', help_text=_('Person who has membership in organization'))
    post = models.ForeignKey('Post', help_text=_('The post held by the member through this membership'))
    organization = models.ForeignKey('Organization',
                                     help_text=_('The organization in which the person or organization is a member'))


class Person(models.Model):
    name = models.CharField(max_length=255, help_text=_("A person's preferred full name"))

    def __str__(self):
        return self.name
