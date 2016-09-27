# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import DataModel


class Person(DataModel):
    name = models.CharField(max_length=255, help_text=_("A person's preferred full name"))
    given_name = models.CharField(max_length=255, help_text=_('One or more primary given names'))
    family_name = models.CharField(max_length=255, help_text=_('One or more family names'))

    # TODO plenty of fields missing

    def __str__(self):
        return self.name


class Membership(DataModel):
    person = models.ForeignKey(Person, related_name='memberships',
                               help_text=_('Person who has membership in organization'))
    organization = models.ForeignKey('Organization', related_name='memberships',
                                     help_text=_('The organization in which the person or organization is a member'))
    # TODO format?
    role = models.CharField(max_length=255, help_text=_("The role that the person fulfills in the organization"),
                            blank=True, null=True)
    start_date = models.DateField(blank=True, null=True, help_text=_('The date on which the relationship began'))
    end_date = models.DateField(blank=True, null=True, help_text=_('The date on which the relationship ended'))

    # TODO plenty of fields missing

    def __str__(self):
        return '{} in {} fullfilling role {}'.format(self.person, self.organization, self.role)
