from rest_framework import serializers, viewsets
from decisions.models import Action, Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        exclude = ('id', 'action')


class ActionSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Action
        fields = '__all__'


class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
