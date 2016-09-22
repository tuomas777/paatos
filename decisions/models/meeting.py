# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel


# Popoloish models


# "An event is an occurrence that people may attend."
class Event(BaseModel):
    name = models.CharField(max_length=255, help_text=_("The event's name"))
    organization = models.ForeignKey('Organization', related_name='events',
                                     help_text=_('The organization organizing the event'))
    attendees = models.ManyToManyField('Person', related_name='events', help_text=_('People attending this event'),
                                       through='Attendance')
    description = models.TextField(help_text=_("The event's description"))
    # TODO type?
    classification = models.CharField(max_length=255, help_text=_("The event's category"))
    parent = models.ForeignKey('self', help_text="The event that this event is a part of", blank=True, null=True)
    # TODO type?
    location = models.CharField(max_length=255, help_text=_("The event's location"))
    start_date = models.DateField(help_text=_('The time at which the event starts'))
    end_date = models.DateField(help_text=_('The time at which the event ends'), blank=True, null=True)

    def __str__(self):
        return self.name


class Attendance(BaseModel):
    event = models.ForeignKey(Event)
    attendee = models.ForeignKey('Person')
    role = models.CharField(max_length=50, help_text=_('Role of the person in the event (chairman, secretary...'))


class VoteCount(BaseModel):
    # TODO type ?
    group = models.CharField(max_length=255, help_text=_('A group of voters'))
    # TODO type ?
    option = models.CharField(max_length=255, help_text=_('An option in a vote event'))
    value = models.IntegerField(help_text=_('The number of votes for an option'))


class VoteEvent(BaseModel):
    legislative_session = models.ForeignKey(Event, help_text=_('The meeting (event) where this vote took place'))
    action = models.ForeignKey('Action', related_name='vote_events',
                               help_text=_('The action to which this vote event applies'))
    organization = models.ForeignKey('Organization', related_name='vote_events',
                                     help_text=_('The organization whose members are voting'))
    # TODO type ?
    result = models.CharField(max_length=255, help_text=_('The result of the vote event'), blank=True)
    counts = models.ForeignKey(VoteCount, related_name='vote_events',
                               help_text=_('The number of votes for options'))
    # TODO ?
    identifier = models.CharField(max_length=255, help_text=_('An issued identifier'))
