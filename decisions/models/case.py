# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel


# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType


class Case(BaseModel):
    iri = models.CharField(max_length=255,
                           help_text=_('IRI for this case'))
    title = models.CharField(max_length=255,
                             help_text=_('Descriptive compact title for this case'))
    summary = models.CharField(max_length=255, blank=True,
                               help_text=_('Summary of this case. Typically a few sentences.'))
    attachments = models.ManyToManyField('Attachment', related_name='cases')
    category = models.CharField(max_length=255, blank=True,
                                help_text=_('Category this case belongs to ("tehtäväluokka")'))
    area = models.ForeignKey('Area', null=True, blank=True, help_text=_('Geographic area this case is related to'))
    originator = models.ForeignKey('Person', blank=True, null=True, related_name='cases',
                                   help_text=_('Person or organization the proposed this case to the city'))
    creation_date = models.DateField(blank=True, null=True, help_text=_('Date this case was entered into system'))
    district = models.CharField(max_length=255, blank=True,
                                help_text=_('Name of district (if any), that this issue is related to. '))
    public = models.BooleanField(default=True, help_text=_('Is this case public?'))
    related_cases = models.ManyToManyField('self', help_text=_('Other cases that are related to this case'))

    def __str__(self):
        return self.title


class Action(BaseModel):
    iri = models.CharField(max_length=255,
                           help_text=_('IRI for this action'))
    title = models.CharField(max_length=255,
                             help_text=_('Title of the action'))
    case = models.ForeignKey(Case, related_name='actions', help_text=_('Case this action is related to'))
    ordering = models.IntegerField(help_text=_('Ordering of this action within a meeting'))
    article_number = models.CharField(max_length=255, null=True,
                                      help_text=_('The article number given to this action after decision'))
    proposal_identifier = models.CharField(max_length=255,
                                           help_text=_(
                                               'Identifier for this action used inside the meeting minutes. '
                                               'The format will vary between cities.'))
    resolution = models.CharField(max_length=255, blank=True, null=True,
                                  help_text="Resolution taken in this action (like tabled, decided...)")
    responsible_party = models.ForeignKey('Organization', related_name='actions', help_text=_(
        'The city organization responsible for this decision. If decision is delegated, this is '
        'the organization that delegated the authority.'))
    delegation = models.ForeignKey('Post', related_name='actions', blank=True, null=True, help_text=_(
        'If this decision was delegated, this field will be filled and refers to the post that made the decision'))
    event = models.ForeignKey('Event', related_name='actions',
                              help_text=_('Event (if any) where this action took place'), null=True)
    # Contents for this action refer to this
    # Votes for this action refer here

    def __str__(self):
        return self.title


class Content(BaseModel):
    iri = models.CharField(max_length=255, help_text=_('IRI for this content'))
    ordering = models.IntegerField(help_text=_('Ordering of this content within the larger context (like action)'))
    title = models.CharField(max_length=255, help_text=_('Title of this content'))
    type = models.CharField(max_length=255, help_text=_(
        'Type of this content (options include: decision, proposal, proceedings...)'))
    hypertext = models.CharField(max_length=255, help_text=_(
        'Content formatted with pseudo-HTML. Only a very restricted set of tags is allowed. '
        'These are: first and second level headings (P+H1+H2) and table (more may be added, '
        'but start from a minimal set)'))
    action = models.ForeignKey(Action, related_name='contents', help_text=_('Action that this content describes'))

    def __str__(self):
        return self.title


class Attachment(BaseModel):
    iri = models.CharField(max_length=255, help_text=_('IRI for this attachment'))
    file = models.CharField(max_length=255, help_text=_('FIXME: i should refer to a file'))
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
