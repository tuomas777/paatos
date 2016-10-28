# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import DataModel


# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
class Category(DataModel):
    name = models.CharField(max_length=255, help_text=_('Name of this category'))
    parent = models.ForeignKey('self', help_text=_('Parent category of this category'), blank=True, null=True)

    def __str__(self):
        # TODO cache
        return '%s / %s' % (self.parent, self.name) if self.parent else self.name


class Case(DataModel):
    iri = models.CharField(max_length=255,
                           help_text=_('IRI for this case'), blank=True)
    title = models.CharField(max_length=255,
                             help_text=_('Descriptive compact title for this case'))
    summary = models.CharField(max_length=255, blank=True,
                               help_text=_('Summary of this case. Typically a few sentences.'))
    register_id = models.CharField(max_length=255, help_text=_('Register ID of this case'), unique=True, db_index=True)
    attachments = models.ManyToManyField('Attachment', related_name='cases')
    category = models.ForeignKey(Category, related_name='cases',
                                 help_text=_('Category this case belongs to ("tehtäväluokka")'))
    area = models.ForeignKey('Area', null=True, blank=True, help_text=_('Geographic area this case is related to'))
    organization = models.ForeignKey('Organization', blank=True, null=True, related_name='cases')
    originator = models.ForeignKey('Person', blank=True, null=True, related_name='cases',
                                   help_text=_('Person who proposed this case to the city'))
    creation_date = models.DateField(blank=True, null=True, help_text=_('Date this case was entered into system'))
    district = models.CharField(max_length=255, blank=True,
                                help_text=_('Name of district (if any), that this issue is related to. '))
    public = models.BooleanField(default=True, help_text=_('Is this case public?'))
    related_cases = models.ManyToManyField('self', help_text=_('Other cases that are related to this case'))

    def __str__(self):
        return self.title


class Action(DataModel):
    iri = models.CharField(max_length=255,
                           help_text=_('IRI for this action'), blank=True)
    title = models.CharField(max_length=255,
                             help_text=_('Title of the action'))
    case = models.ForeignKey(Case, related_name='actions', help_text=_('Case this action is related to'), blank=True,
                             null=True)
    ordering = models.IntegerField(help_text=_('Ordering of this action within a meeting'))
    article_number = models.CharField(max_length=255, blank=True,
                                      help_text=_('The article number given to this action after decision'))
    proposal_identifier = models.CharField(max_length=255, blank=True,
                                           help_text=_(
                                               'Identifier for this action used inside the meeting minutes. '
                                               'The format will vary between cities.'))
    resolution = models.CharField(max_length=255, blank=True,
                                  help_text="Resolution taken in this action (like tabled, decided...)")
    responsible_party = models.ForeignKey('Organization', related_name='actions', help_text=_(
        'The city organization responsible for this decision. If decision is delegated, this is '
        'the organization that delegated the authority.'), blank=True, null=True)
    delegation = models.ForeignKey('Post', related_name='actions', blank=True, null=True, help_text=_(
        'If this decision was delegated, this field will be filled and refers to the post that made the decision'))
    event = models.ForeignKey('Event', related_name='actions', help_text=_('Event this action is related to'))

    # Contents for this action refer to this
    # Votes for this action refer here

    def __str__(self):
        return self.title


class Content(DataModel):
    iri = models.CharField(max_length=255, help_text=_('IRI for this content'), blank=True)
    ordering = models.IntegerField(help_text=_('Ordering of this content within the larger context (like action)'))
    title = models.CharField(max_length=255, help_text=_('Title of this content'), blank=True)
    type = models.CharField(max_length=255, help_text=_(
        'Type of this content (options include: decision, proposal, proceedings...)'))
    hypertext = models.TextField(help_text=_(
        'Content formatted with pseudo-HTML. Only a very restricted set of tags is allowed. '
        'These are: first and second level headings (P+H1+H2) and table (more may be added, '
        'but start from a minimal set)'))
    action = models.ForeignKey(Action, related_name='contents', help_text=_('Action that this content describes'))

    def __str__(self):
        return '%s %s' % (self.action, self.ordering)


class Attachment(DataModel):
    iri = models.CharField(max_length=255, help_text=_('IRI for this attachment'), blank=True)
    file = models.CharField(max_length=255, help_text=_('FIXME: i should refer to a file'))
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
