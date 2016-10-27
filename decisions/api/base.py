from rest_framework import serializers


class DataModelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    data_source = serializers.SlugRelatedField('identifier', read_only=True)
