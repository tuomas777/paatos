import django_filters
from rest_framework import serializers


class BaseFilter(django_filters.rest_framework.FilterSet):
    modified_at_gte = django_filters.DateTimeFilter(name='modified_at', lookup_expr='gte')
    modified_at_lte = django_filters.DateTimeFilter(name='modified_at', lookup_expr='lte')

    class Meta:
        fields = ('modified_at_gte', 'modified_at_lte')


class DataModelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    data_source = serializers.SlugRelatedField('identifier', read_only=True)
