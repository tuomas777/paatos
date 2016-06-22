# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
from .organization import Organization  # noqa
from .organization import Post  # noqa
from .person import Person  # noqa
from .meeting import Event  # noqa


class Case(models.Model):
    iri = models.CharField(max_length=255,
                           help_text=_('IRI for this case'))
    title = models.CharField(max_length=255,
                             help_text=_('A high level matter to be decided'))
    description = models.CharField(max_length=255, blank=True,
                                   help_text=_('A descriptive compact title for the case'))
    summary = models.CharField(max_length=255, blank=True,
                               help_text=_('Summary of this case. Typically a few sentences.'))
    attachments = models.ManyToManyField('Attachment')
    category = models.CharField(max_length=255, blank=True,
                                help_text=_('Category this case belongs to ("tehtäväluokka")'))
    # area = models.ForeignKey('Area', null=True,
    #                          help_text=_('Geographic area this case is related to'))
    originator = models.ForeignKey('Person', null=True)
    creation_date = models.DateField(blank=True, null=True)
    public = models.BooleanField(default=True)
    related_case = models.ManyToManyField('self', help_text=_('Other related cases'))

    def __str__(self):
        return self.title


class Action(models.Model):
    iri = models.CharField(max_length=255,
                           help_text=_('IRI for this action'))
    title = models.CharField(max_length=255,
                             help_text=_('Descriptive compact title for this case'))
    case = models.ForeignKey(Case, help_text=_('Case this action affects'))
    ordering = models.IntegerField(help_text=_('Ordering of this action within a meeting'))
    article_number = models.CharField(max_length=255, null=True,
                                      help_text=_('The article number given to this action after decision'))
    proposal_identifier = models.CharField(max_length=255,
                                           help_text=_(
                                               'Identifier for this action used inside the meeting minutes. '
                                               'The format will vary between cities.'))
    resolution = models.CharField(max_length=255, blank=True, null=True,
                                  help_text="Resolution taken in this action (like tabled, decided...)")
    responsible_party = models.ForeignKey('Organization', help_text=_(
        'The city organization responsible for this decision. If decision is delegated, this is '
        'the organization that delegated the authority.'))
    delegation = models.ForeignKey('Post', blank=True, null=True, help_text=_(
        'If this decision was delegated, this field will be filled and refers to the post that made the decision'))
    event = models.ForeignKey('Event', help_text=_('Event (if any) where this action took place'), null=True)
    # Contents for this action refer to this
    # Votes for this action refer here

    def __str__(self):
        return self.title


class Content(models.Model):
    iri = models.CharField(max_length=255, help_text=_('IRI for this content'))
    ordering = models.IntegerField(help_text=_('Ordering of this content within the larger context (like action)'))
    title = models.CharField(max_length=255, help_text=_('Title of this content'))
    type = models.CharField(max_length=255, help_text=_(
        'Type of this content (options include: decision, proposal, proceedings...)'))
    hypertext = models.CharField(max_length=255, help_text=_(
        'Content formatted with pseudo-HTML. Only a very restricted set of tags is allowed. '
        'These are: first and second level headings (P+H1+H2) and table (more may be added, '
        'but start from a minimal set)'))
    action = models.ForeignKey('Action', help_text=_('Action that this content describes'))

    def __str__(self):
        return self.title


class Attachment(models.Model):
    iri = models.CharField(max_length=255, help_text=_('IRI for this attachment'))
    file = models.CharField(max_length=255, help_text=_('FIXME: i should refer to a file'))
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
