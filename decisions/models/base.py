# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False,
                                      help_text=_('The time at which the resource was created'))
    modified_at = models.DateTimeField(auto_now=True, editable=False,
                                       help_text=_('The time at which the resource was updated'))

    class Meta:
        abstract = True
