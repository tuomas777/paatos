from rest_framework import viewsets
from decisions.models import Action, Content
from .base import DataModelSerializer


class ContentSerializer(DataModelSerializer):
    class Meta:
        model = Content
        exclude = ('url', 'id', 'action')


class ActionSerializer(DataModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Action
        fields = '__all__'


class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
