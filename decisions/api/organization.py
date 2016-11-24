from rest_framework import serializers, viewsets

from decisions.models import Event, Organization, Post

from .base import DataModelSerializer


class OrganizationSerializer(DataModelSerializer):
    events = serializers.HyperlinkedRelatedField(queryset=Event.objects.all(), view_name='event-detail', many=True)
    posts = serializers.HyperlinkedRelatedField(queryset=Post.objects.all(), view_name='post-detail', many=True)

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.select_related('data_source').prefetch_related('events', 'posts')
    serializer_class = OrganizationSerializer
