# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import DataModel


class Organization(DataModel):
    abstract = models.CharField(max_length=255, help_text=_('A one-line description of an organization'), blank=True)
    description = models.TextField(help_text=_('An extended description of an organization'), blank=True)
    classification = models.CharField(max_length=255, help_text=_('An organization category, e.g. committee'))
    name = models.CharField(max_length=255, help_text=_('A primary name, e.g. a legally recognized name'))
    founding_date = models.DateField(help_text=_('A date of founding'), blank=True, null=True)
    dissolution_date = models.DateField(help_text=_('A date of dissolution'), blank=True, null=True)
    parent = models.ForeignKey('self', help_text=_('The organizations that contain this organization'), null=True,
                               blank=True)
    area = models.ForeignKey('Area', related_name='organizations', blank=True, null=True,
                             help_text=_('The geographic area to which this organization is related'))
    image = models.URLField(help_text=_('A URL of an image'), blank=True)

    def __str__(self):
        if self.parent:
            return '%s / %s' % (self.parent, self.name)  # TODO cache
        else:
            return self.name


class Post(DataModel):
    label = models.CharField(max_length=255, help_text=_('A label describing the post'))
    organization = models.ForeignKey(Organization, help_text=_('The organization in which the post is held'))
    area = models.ForeignKey('Area', related_name='posts', blank=True, null=True,
                             help_text=_('The geographic area to which this post is related'))
    start_date = models.DateField(help_text=_('The date on which the post was created'), null=True, blank=True)
    end_date = models.DateField(help_text=_('The date on which the post was eliminated'), null=True, blank=True)
    memberships = models.ManyToManyField('Membership', related_name='posts',
                                         help_text=_('The memberships of the members of the organization and of the '
                                                     'organization itself'))
    role = models.CharField(max_length=255, help_text=_('The function that the holder of the post fulfills'),
                            blank=True)
    other_label = models.CharField(max_length=255, help_text=_('An alternate label'), blank=True)

    def __str__(self):
        return '%s / %s' % (self.organization, self.label)  # TODO cache
