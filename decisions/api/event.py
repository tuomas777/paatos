from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets
from decisions.models import Action, Event
from .base import BaseFilter, DataModelSerializer


class EventFilter(BaseFilter):
    class Meta:
        model = Event
        fields = BaseFilter.Meta.fields + ('organization',)


class EventSerializer(DataModelSerializer):
    actions = serializers.HyperlinkedRelatedField(queryset=Action.objects.all(), many=True, view_name='action-detail')

    class Meta:
        model = Event
        fields = '__all__'


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EventFilter
