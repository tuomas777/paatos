from rest_framework import viewsets
from decisions.models import Organization
from .base import DataModelSerializer


class OrganizationSerializer(DataModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
