# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .person import Person  # noqa
from .organization import Organization  # noqa

# Popoloish models


# "An event is an occurrence that people may attend."
class Event(models.Model):
    name = models.CharField(max_length=255, help_text=_("The event's name"))
    organization = models.ForeignKey('Organization', help_text=_('The organization organizing the event'))
    attendees = models.ManyToManyField('Person', help_text=_('People attending this event'), through='Attendance')

    def __str__(self):
        return self.name


class Attendance(models.Model):
    event = models.ForeignKey('Event')
    attendee = models.ForeignKey('Person')
    role = models.CharField(max_length=50, help_text=_('Role of the person in the event (chairman, secretary...'))


class VoteEvent(models.Model):
    legislative_session = models.ForeignKey('Event', help_text=_('The meeting (event) where this vote took place'))
    vote_count = models.ForeignKey('VoteCount')


class VoteCount(models.Model):
    pass
