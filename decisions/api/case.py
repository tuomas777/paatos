from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, serializers, viewsets
from decisions.models import Action, Case
from .base import BaseFilter, DataModelSerializer


class CaseFilter(BaseFilter):
    class Meta:
        model = Case
        fields = BaseFilter.Meta.fields + ('register_id',)


class CaseSerializer(DataModelSerializer):
    actions = serializers.HyperlinkedRelatedField(queryset=Action.objects.all(), many=True, view_name='action-detail')

    class Meta:
        model = Case
        exclude = ('related_cases',)


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.select_related('data_source').prefetch_related('actions', 'attachments')
    serializer_class = CaseSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_class = CaseFilter
    search_fields = ('title', 'summary')
