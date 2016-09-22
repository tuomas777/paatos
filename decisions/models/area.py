# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel


class Area(BaseModel):
    name = models.CharField(max_length=255, help_text=_("Area's name"))
    parent = models.ForeignKey('self', help_text=_('The area that contains this area'))
    # TODO type?
    classification = models.CharField(max_length=255, help_text=_('An area category, e.g. city'), blank=True)

    # TODO geometry

    identifier = models.CharField(max_length=255, help_text=_('An issued identifier'), blank=True)

    def __str__(self):
        return self.name
