from rest_framework import viewsets
from decisions.models import Event
from .base import DataModelSerializer


class EventSerializer(DataModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
