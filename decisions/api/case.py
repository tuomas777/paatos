from rest_framework import filters, serializers, viewsets
from decisions.models import Action, Case
from .base import DataModelSerializer


class CaseSerializer(DataModelSerializer):
    actions = serializers.HyperlinkedRelatedField(queryset=Action.objects.all(), many=True, view_name='action-detail')

    class Meta:
        model = Case
        fields = '__all__'


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'summary')
