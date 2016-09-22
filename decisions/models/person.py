# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel


class Person(BaseModel):
    name = models.CharField(max_length=255, help_text=_("A person's preferred full name"))
    # TODO plenty of fields missing

    def __str__(self):
        return self.name


class Membership(BaseModel):
    person = models.ForeignKey(Person, related_name='memberships',
                               help_text=_('Person who has membership in organization'))
    organization = models.ForeignKey('Organization', related_name='memberships',
                                     help_text=_('The organization in which the person or organization is a member'))
    # TODO plenty of fields missing
