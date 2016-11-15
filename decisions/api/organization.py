from rest_framework import serializers, viewsets
from decisions.models import Event, Organization
from .base import DataModelSerializer


class OrganizationSerializer(DataModelSerializer):
    events = serializers.HyperlinkedRelatedField(queryset=Event.objects.all(), view_name='event-detail', many=True)

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.select_related('data_source').prefetch_related('events')
    serializer_class = OrganizationSerializer
