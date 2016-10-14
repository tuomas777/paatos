from rest_framework import serializers, viewsets
from decisions.models import Case


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'



class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
