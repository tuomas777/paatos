from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from decisions.models import Action, Content
from .base import BaseFilter, DataModelSerializer


class ContentSerializer(DataModelSerializer):
    class Meta:
        model = Content
        exclude = ('url', 'id', 'action')


class ActionFilter(BaseFilter):
    class Meta:
        model = Action
        fields = BaseFilter.Meta.fields + ('case', 'event')


class ActionSerializer(DataModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Action
        fields = '__all__'


class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_class = ActionFilter
    search_fields = ('title', 'contents__hypertext')
