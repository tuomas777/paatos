from rest_framework import viewsets
from decisions.models import Case
from .base import DataModelSerializer


class CaseSerializer(DataModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
